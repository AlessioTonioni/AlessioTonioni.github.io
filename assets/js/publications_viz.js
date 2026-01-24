document.addEventListener('DOMContentLoaded', function () {
    // Fetch the enhanced publications data
    fetch('/assets/data/publications_enhanced.json')
        .then(response => response.json())
        .then(data => {
            renderStats(data.stats);
            renderMap(data.publications, 'umap');
            window.pubData = data.publications; // Store for toggling
        })
        .catch(err => {
            console.error("Error loading publication data:", err);
            document.getElementById('pub-stats').innerHTML = '<p style="color: #999;">Unable to load statistics.</p>';
            document.getElementById('pub-map').innerHTML = '<p style="color: #999;">Unable to load map.</p>';
        });
});

function renderStats(stats) {
    if (!stats) return;

    // Render top 5 authors
    const authorsHTML = stats.top_cited_authors
        .map((a, i) => `${i + 1}. ${a.name} <span style="opacity:0.8">(${a.count}×)</span>`)
        .join('<br>');
    document.getElementById('stat-authors').innerHTML = authorsHTML;

    // Render top 5 papers
    const papersHTML = stats.top_cited_papers
        .map((p, i) => {
            const title = p.title.length > 50 ? p.title.substring(0, 50) + '...' : p.title;
            return `${i + 1}. ${title} <span style="opacity:0.8">(${p.count}×)</span>`;
        })
        .join('<br>');
    document.getElementById('stat-papers').innerHTML = papersHTML;

    document.getElementById('stat-year').textContent =
        `${stats.most_influential_year.year} (${stats.most_influential_year.count} papers)`;
}

function renderMap(pubs, mode) {
    // Filter publications that have map coordinates
    const validPubs = pubs.filter(p => p.map_coords && p.map_coords[mode]);

    if (validPubs.length === 0) {
        document.getElementById('pub-map').innerHTML =
            '<p style="color: #999; text-align: center; padding: 40px;">No map data available yet.</p>';
        return;
    }

    // Group by category for colors
    const categories = [...new Set(validPubs.map(p =>
        p.ai_results ? p.ai_results.category : 'Uncategorized'
    ))];

    // Color palette - vibrant, distinct colors
    const categoryColors = [
        '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
        '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'
    ];

    const traces = [];

    // Create edges and markers for each category
    categories.forEach((cat, i) => {
        const catPubs = validPubs.filter(p =>
            (p.ai_results ? p.ai_results.category : 'Uncategorized') === cat
        );

        const color = categoryColors[i % categoryColors.length];

        // Add edges connecting papers in the same category
        if (catPubs.length > 1) {
            const edgeX = [];
            const edgeY = [];

            // Connect each paper to its nearest neighbors in the same category
            catPubs.forEach((pub1, idx1) => {
                const x1 = pub1.map_coords[mode].x;
                const y1 = pub1.map_coords[mode].y;

                // Find 2 nearest neighbors
                const distances = catPubs
                    .map((pub2, idx2) => {
                        if (idx1 === idx2) return { idx: idx2, dist: Infinity };
                        const x2 = pub2.map_coords[mode].x;
                        const y2 = pub2.map_coords[mode].y;
                        const dist = Math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2);
                        return { idx: idx2, dist };
                    })
                    .sort((a, b) => a.dist - b.dist)
                    .slice(0, 2);

                distances.forEach(({ idx }) => {
                    const x2 = catPubs[idx].map_coords[mode].x;
                    const y2 = catPubs[idx].map_coords[mode].y;
                    edgeX.push(x1, x2, null);
                    edgeY.push(y1, y2, null);
                });
            });

            // Add edge trace
            traces.push({
                x: edgeX,
                y: edgeY,
                mode: 'lines',
                type: 'scatter',
                line: {
                    color: color,
                    width: 1,
                    opacity: 0.2
                },
                hoverinfo: 'skip',
                showlegend: false
            });
        }

        // Add marker trace
        traces.push({
            x: catPubs.map(p => p.map_coords[mode].x),
            y: catPubs.map(p => p.map_coords[mode].y),
            text: catPubs.map(p => {
                const summary = p.ai_results ? p.ai_results.summary : 'No summary available';
                return `<b>${p.title}</b><br><br>${summary}`;
            }),
            mode: 'markers',
            type: 'scatter',
            name: cat,
            marker: {
                // Size based on year (newer = larger): 2026 -> 25px, 2017 -> 8px
                size: catPubs.map(p => {
                    const year = p.s2_metadata ? p.s2_metadata.year : (new Date(p.date).getFullYear() || 2020);
                    const currentYear = new Date().getFullYear();
                    // Map range [current-10, current] to [5, 25]
                    const age = Math.max(0, currentYear - year);
                    return Math.max(5, 25 - age);
                }),
                color: color,
                line: { color: 'white', width: 1.5 },
                opacity: 1.0
            },
            hoverinfo: 'text',
            customdata: catPubs.map(p => ({
                permalink: p.permalink,
                title: p.title
            }))
        });
    });

    const layout = {
        hovermode: 'closest',
        showlegend: true,
        legend: {
            orientation: 'v',
            x: 1.02,
            y: 1,
            xanchor: 'left',
            font: { size: 11 }
        },
        margin: { l: 40, r: 200, b: 40, t: 20 },
        xaxis: {
            showgrid: false,
            zeroline: false,
            showticklabels: false,
            title: ''
        },
        yaxis: {
            showgrid: false,
            zeroline: false,
            showticklabels: false,
            title: ''
        },
        plot_bgcolor: 'rgba(250,250,250,0.5)',
        paper_bgcolor: 'rgba(0,0,0,0)',
        font: { family: 'system-ui, -apple-system, sans-serif' }
    };

    const config = {
        responsive: true,
        displayModeBar: false
    };

    Plotly.newPlot('pub-map', traces, layout, config);

    // Handle clicks - scroll to paper in the list
    document.getElementById('pub-map').on('plotly_click', function (data) {
        const point = data.points[0];
        if (!point.customdata) return; // Skip edge clicks

        const title = point.customdata.title;

        // Find all links on the page
        const links = document.querySelectorAll('a');
        for (let link of links) {
            if (link.textContent.trim() === title) {
                // Highlight and scroll
                link.scrollIntoView({ behavior: 'smooth', block: 'center' });
                link.style.backgroundColor = '#fff9c4';
                setTimeout(() => link.style.backgroundColor = 'transparent', 2000);
                break;
            }
        }
    });
}

window.updateMap = function (mode) {
    // Update button states
    const buttons = document.querySelectorAll('.toggle-btn');
    buttons.forEach(btn => {
        if (btn.textContent.toLowerCase().includes(mode)) {
            btn.classList.add('active');
        } else {
            btn.classList.remove('active');
        }
    });

    renderMap(window.pubData, mode);
};
