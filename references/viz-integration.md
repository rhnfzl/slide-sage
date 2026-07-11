# Chart & Visualization Library Integration Guide

## Decision Matrix

| Content Type | Library | CDN URL (exact, versioned) | Gzip Size |
|---|---|---|---|
| Bar, line, pie, doughnut, scatter, radar, polar, bubble | Chart.js 4.4 | `https://cdn.jsdelivr.net/npm/chart.js@4.4.7/dist/chart.umd.min.js` | ~65KB |
| Heatmap, sankey, treemap, candlestick, funnel | ECharts 5.5 | `https://cdn.jsdelivr.net/npm/echarts@5.5.1/dist/echarts.min.js` | ~135KB |
| Custom/bespoke statistical | D3.js v7 | `https://cdn.jsdelivr.net/npm/d3@7.9.0/dist/d3.min.js` | ~80KB |
| Network/dependency graph | Sigma.js v3 + graphology | `https://cdn.jsdelivr.net/npm/sigma@3.0.0/build/sigma.min.js` + `https://cdn.jsdelivr.net/npm/graphology@0.25.4/dist/graphology.umd.min.js` | ~60KB+20KB |
| Calendar heatmap | Frappe Charts | `https://cdn.jsdelivr.net/npm/frappe-charts@2.0.0/dist/frappe-charts.min.umd.js` | ~35KB |

**Selection rule**: Use Chart.js unless the chart type requires another library. Chart.js covers 80%+ of presentation needs with the smallest footprint.

---

## Chart.js Complete Patterns (DEFAULT Library)

### Setup

```html
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.7/dist/chart.umd.min.js"></script>
```

### Responsive Container Pattern

Always wrap canvas in a constrained container. Never set width/height on the canvas element directly.

```html
<div style="position:relative; max-height:min(55vh,420px); width:100%; margin:0 auto;">
  <canvas id="myChart"></canvas>
</div>
```

### Dark Mode Integration

Canvas charts need concrete values, so read the selected presentation tokens at runtime.

```javascript
const theme = getComputedStyle(document.documentElement);
Chart.defaults.color = theme.getPropertyValue('--color-text-secondary').trim() || '#4A6178';
Chart.defaults.borderColor = theme.getPropertyValue('--color-border').trim() || 'rgba(74, 97, 120, 0.18)';
```

Place this **before** any `new Chart()` calls.

### Colorblind-Safe Palette

```javascript
const PALETTE = ['#0077BB', '#CC3311', '#009988', '#EE7733',
  '#3344AA', '#EE3377', '#BBAA33', '#888888'];
```

### Animation Config

Respect the presentation's shared animation level:

```javascript
// animLevel: 'minimal' | 'balanced' | 'dramatic'
function chartAnimation(level = document.documentElement.dataset.animLevel || 'balanced', reducedMotion = false) {
  if (reducedMotion || level === 'minimal') return false;
  const duration = { balanced: 800, dramatic: 1200 }[level] || 800;
  return { duration, easing: 'easeOutQuart' };
}
```

### Slide-Enter Lifecycle

Create every chart with `animation: false`. The canonical `SlidePresentation` class emits a `slidechange` event after the active slide changes, including the first slide after the current DOM-ready turn. Attach the listener while creating each chart so an inactive chart stays still until the audience reaches it.

```javascript
function replayChartOnSlideEnter(chart, reducedMotion) {
  chart.stop();
  const animation = chartAnimation(undefined, reducedMotion);
  if (!animation) {
    chart.options.animation = false;
    chart.update('none');
    return;
  }

  chart.options.animation = animation;
  chart.reset();
  chart.update();
}

const canvas = document.getElementById('barChart');
const chart = new Chart(canvas, {
  type: 'bar',
  data: chartData,
  options: { responsive: true, maintainAspectRatio: false, animation: false }
});

document.addEventListener('slidechange', ({ detail }) => {
  if (detail.slide.contains(canvas)) {
    replayChartOnSlideEnter(chart, detail.reducedMotion);
  }
});
```

For a multi-chart slide, keep each instance in an array and replay only the charts whose canvases are inside `detail.slide`. For CountUp, write the final value directly when `detail.reducedMotion` is true; otherwise reset and start it from this same event. Do not use scroll spying for slide-entry counters.

---

### Bar Chart

```html
<div style="position:relative; max-height:min(55vh,420px); width:100%; margin:0 auto;">
  <canvas id="barChart"></canvas>
</div>
<script>
new Chart(document.getElementById('barChart'), {
  type: 'bar',
  data: {
    labels: ['Q1', 'Q2', 'Q3', 'Q4'],
    datasets: [{
      label: 'Revenue ($M)',
      data: [12, 19, 8, 15],
      backgroundColor: ['#0077BB', '#EE7733', '#009988', '#CC3311'],
      borderRadius: 6,
      borderSkipped: false
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    animation: false,
    plugins: {
      legend: { display: false },
      title: { display: true, text: 'Quarterly Revenue', font: { size: 16, weight: '600' } }
    },
    scales: {
      y: { beginAtZero: true, grid: { color: 'rgba(128,128,128,0.15)' } },
      x: { grid: { display: false } }
    }
  }
});
</script>
```

### Line Chart

```html
<div style="position:relative; max-height:min(55vh,420px); width:100%; margin:0 auto;">
  <canvas id="lineChart"></canvas>
</div>
<script>
new Chart(document.getElementById('lineChart'), {
  type: 'line',
  data: {
    labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    datasets: [{
      label: 'Users',
      data: [120, 190, 300, 250, 420, 380],
      borderColor: '#0077BB',
      backgroundColor: 'rgba(0,119,187,0.1)',
      fill: true,
      tension: 0.35,
      pointRadius: 4,
      pointHoverRadius: 7,
      pointBackgroundColor: '#0077BB',
      pointBorderColor: '#fff',
      pointBorderWidth: 2
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    animation: false,
    plugins: {
      legend: { position: 'top', labels: { usePointStyle: true } }
    },
    scales: {
      y: { beginAtZero: true, grid: { color: 'rgba(128,128,128,0.15)' } },
      x: { grid: { display: false } }
    }
  }
});
</script>
```

### Pie / Doughnut Chart

```html
<div style="position:relative; max-height:min(50vh,380px); width:min(50vh,380px); margin:0 auto;">
  <canvas id="doughnutChart"></canvas>
</div>
<script>
new Chart(document.getElementById('doughnutChart'), {
  type: 'doughnut', // Change to 'pie' for solid fill
  data: {
    labels: ['Frontend', 'Backend', 'DevOps', 'QA'],
    datasets: [{
      data: [35, 30, 20, 15],
      backgroundColor: ['#0077BB', '#EE7733', '#009988', '#3344AA'],
      borderWidth: 2,
      borderColor: 'transparent',
      hoverOffset: 8
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    cutout: '55%', // Remove for pie chart
    animation: false,
    plugins: {
      legend: { position: 'right', labels: { usePointStyle: true, padding: 16 } }
    }
  }
});
</script>
```

### Scatter Chart

```html
<div style="position:relative; max-height:min(55vh,420px); width:100%; margin:0 auto;">
  <canvas id="scatterChart"></canvas>
</div>
<script>
new Chart(document.getElementById('scatterChart'), {
  type: 'scatter',
  data: {
    datasets: [{
      label: 'Performance',
      data: [
        { x: 10, y: 20 }, { x: 15, y: 10 }, { x: 25, y: 30 },
        { x: 30, y: 25 }, { x: 45, y: 40 }, { x: 55, y: 35 }
      ],
      backgroundColor: 'rgba(0,119,187,0.6)',
      pointRadius: 6,
      pointHoverRadius: 9
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    animation: false,
    scales: {
      x: { title: { display: true, text: 'Latency (ms)' }, grid: { color: 'rgba(128,128,128,0.15)' } },
      y: { title: { display: true, text: 'Throughput (req/s)' }, grid: { color: 'rgba(128,128,128,0.15)' } }
    }
  }
});
</script>
```

### Radar Chart

```html
<div style="position:relative; max-height:min(50vh,380px); width:min(50vh,380px); margin:0 auto;">
  <canvas id="radarChart"></canvas>
</div>
<script>
new Chart(document.getElementById('radarChart'), {
  type: 'radar',
  data: {
    labels: ['Speed', 'Reliability', 'Scalability', 'Security', 'Usability'],
    datasets: [{
      label: 'Current',
      data: [65, 80, 70, 90, 75],
      borderColor: '#0077BB',
      backgroundColor: 'rgba(0,119,187,0.15)',
      pointBackgroundColor: '#0077BB',
      pointBorderColor: '#fff',
      pointBorderWidth: 2
    }, {
      label: 'Target',
      data: [85, 90, 85, 95, 90],
      borderColor: '#009988',
      backgroundColor: 'rgba(0,153,136,0.1)',
      pointBackgroundColor: '#009988',
      pointBorderColor: '#fff',
      pointBorderWidth: 2
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    animation: false,
    scales: {
      r: {
        beginAtZero: true,
        max: 100,
        grid: { color: 'rgba(128,128,128,0.15)' },
        angleLines: { color: 'rgba(128,128,128,0.15)' }
      }
    },
    plugins: {
      legend: { position: 'top', labels: { usePointStyle: true } }
    }
  }
});
</script>
```

### Multi-Chart Slide (Side-by-Side)

```html
<div style="display:flex; gap:2rem; align-items:stretch; width:100%; max-height:min(55vh,420px);">
  <div style="flex:1; position:relative; min-width:0;">
    <canvas id="chartLeft"></canvas>
  </div>
  <div style="flex:1; position:relative; min-width:0;">
    <canvas id="chartRight"></canvas>
  </div>
</div>
<script>
// Create two charts with the same options pattern
new Chart(document.getElementById('chartLeft'), {
  type: 'bar',
  data: {
    labels: ['A', 'B', 'C'],
    datasets: [{ label: 'Series 1', data: [10, 20, 30], backgroundColor: '#0077BB', borderRadius: 6 }]
  },
  options: { responsive: true, maintainAspectRatio: false, animation: false, plugins: { legend: { display: false } } }
});
new Chart(document.getElementById('chartRight'), {
  type: 'line',
  data: {
    labels: ['A', 'B', 'C'],
    datasets: [{ label: 'Series 2', data: [30, 15, 25], borderColor: '#EE7733', tension: 0.3, pointRadius: 4 }]
  },
  options: { responsive: true, maintainAspectRatio: false, animation: false, plugins: { legend: { display: false } } }
});
</script>
```

---

## ECharts Patterns (Advanced)

### Setup

```html
<script src="https://cdn.jsdelivr.net/npm/echarts@5.5.1/dist/echarts.min.js"></script>
```

### Responsive Resize Handler

```javascript
const chart = echarts.init(document.getElementById('echartDiv'));
chart.setOption(option);
window.addEventListener('resize', () => chart.resize());
```

### Heatmap

```html
<div id="heatmapChart" style="width:100%; height:min(55vh,420px);"></div>
<script>
const chart = echarts.init(document.getElementById('heatmapChart'));
const hours = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'];
const metrics = ['CPU', 'Memory', 'Disk', 'Network'];
const data = [
  [0,0,45],[0,1,60],[0,2,30],[0,3,70],
  [1,0,55],[1,1,80],[1,2,40],[1,3,50],
  [2,0,35],[2,1,45],[2,2,90],[2,3,60],
  [3,0,65],[3,1,70],[3,2,55],[3,3,85],
  [4,0,50],[4,1,35],[4,2,60],[4,3,40]
];
chart.setOption({
  tooltip: { position: 'top' },
  grid: { left: 80, right: 20, top: 20, bottom: 40 },
  xAxis: { type: 'category', data: metrics, splitArea: { show: true } },
  yAxis: { type: 'category', data: hours, splitArea: { show: true } },
  visualMap: { min: 0, max: 100, calculable: true, orient: 'horizontal', left: 'center', bottom: 0,
    inRange: { color: ['#009988', '#EE7733', '#CC3311'] }
  },
  series: [{ type: 'heatmap', data, label: { show: true }, emphasis: { itemStyle: { shadowBlur: 10 } } }]
});
window.addEventListener('resize', () => chart.resize());
</script>
```

### Sankey Diagram

```html
<div id="sankeyChart" style="width:100%; height:min(55vh,420px);"></div>
<script>
const chart = echarts.init(document.getElementById('sankeyChart'));
chart.setOption({
  tooltip: { trigger: 'item' },
  series: [{
    type: 'sankey',
    layout: 'none',
    emphasis: { focus: 'adjacency' },
    data: [
      { name: 'Source A' }, { name: 'Source B' },
      { name: 'Process X' }, { name: 'Process Y' },
      { name: 'Output 1' }, { name: 'Output 2' }
    ],
    links: [
      { source: 'Source A', target: 'Process X', value: 30 },
      { source: 'Source A', target: 'Process Y', value: 20 },
      { source: 'Source B', target: 'Process X', value: 10 },
      { source: 'Source B', target: 'Process Y', value: 40 },
      { source: 'Process X', target: 'Output 1', value: 25 },
      { source: 'Process X', target: 'Output 2', value: 15 },
      { source: 'Process Y', target: 'Output 1', value: 35 },
      { source: 'Process Y', target: 'Output 2', value: 25 }
    ],
    lineStyle: { color: 'gradient', curveness: 0.5 }
  }]
});
window.addEventListener('resize', () => chart.resize());
</script>
```

### Treemap

```html
<div id="treemapChart" style="width:100%; height:min(55vh,420px);"></div>
<script>
const chart = echarts.init(document.getElementById('treemapChart'));
chart.setOption({
  tooltip: { formatter: '{b}: {c}' },
  series: [{
    type: 'treemap',
    roam: false,
    breadcrumb: { show: false },
    label: { show: true, formatter: '{b}\n{c}', fontSize: 13 },
    data: [
      { name: 'Frontend', value: 35, itemStyle: { color: '#0077BB' },
        children: [
          { name: 'React', value: 20 }, { name: 'Vue', value: 10 }, { name: 'Angular', value: 5 }
        ]
      },
      { name: 'Backend', value: 30, itemStyle: { color: '#009988' },
        children: [
          { name: 'Node.js', value: 15 }, { name: 'Python', value: 10 }, { name: 'Go', value: 5 }
        ]
      },
      { name: 'DevOps', value: 20, itemStyle: { color: '#EE7733' } },
      { name: 'QA', value: 15, itemStyle: { color: '#3344AA' } }
    ]
  }]
});
window.addEventListener('resize', () => chart.resize());
</script>
```

### ECharts Theme Integration

```javascript
// Match presentation dark mode
const isDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
const chart = echarts.init(document.getElementById('echartDiv'), isDark ? 'dark' : null);
```

---

## D3.js Patterns (Custom)

### Setup

```html
<script src="https://cdn.jsdelivr.net/npm/d3@7.9.0/dist/d3.min.js"></script>
```

### Simple SVG Bar Chart in a Slide

```html
<div id="d3chart" style="width:100%; max-height:min(55vh,420px);"></div>
<script>
const data = [
  { label: 'A', value: 30 }, { label: 'B', value: 80 },
  { label: 'C', value: 45 }, { label: 'D', value: 60 }, { label: 'E', value: 20 }
];
const container = document.getElementById('d3chart');
const width = container.clientWidth;
const height = Math.min(window.innerHeight * 0.55, 420);
const margin = { top: 20, right: 20, bottom: 30, left: 40 };

const svg = d3.select('#d3chart').append('svg')
  .attr('viewBox', `0 0 ${width} ${height}`)
  .attr('preserveAspectRatio', 'xMidYMid meet')
  .style('width', '100%').style('height', 'auto');

const x = d3.scaleBand().domain(data.map(d => d.label)).range([margin.left, width - margin.right]).padding(0.3);
const y = d3.scaleLinear().domain([0, d3.max(data, d => d.value)]).nice().range([height - margin.bottom, margin.top]);

svg.selectAll('rect').data(data).join('rect')
  .attr('x', d => x(d.label)).attr('y', d => y(d.value))
  .attr('width', x.bandwidth()).attr('height', d => y(0) - y(d.value))
  .attr('rx', 4).attr('fill', '#0077BB');

svg.append('g').attr('transform', `translate(0,${height - margin.bottom})`).call(d3.axisBottom(x));
svg.append('g').attr('transform', `translate(${margin.left},0)`).call(d3.axisLeft(y).ticks(5));
</script>
```

### Responsive viewBox Pattern

```javascript
// Always use viewBox instead of fixed width/height for responsive D3
const svg = d3.select('#container').append('svg')
  .attr('viewBox', '0 0 800 450')
  .attr('preserveAspectRatio', 'xMidYMid meet')
  .style('width', '100%')
  .style('height', 'auto')
  .style('max-height', 'min(55vh, 420px)');
```

---

## Data Input Patterns

### Inline JSON (Direct in Script)

Most common for presentations -- data is embedded directly in the chart config.

```javascript
const data = {
  labels: ['Q1', 'Q2', 'Q3', 'Q4'],
  values: [120, 190, 300, 250]
};
```

### CSV Parsing (No Library)

For user-provided CSV data, parse with a simple string split (no Papa Parse needed for small datasets).

```javascript
function parseCSV(csv) {
  const lines = csv.trim().split('\n');
  const headers = lines[0].split(',').map(h => h.trim());
  return lines.slice(1).map(line => {
    const vals = line.split(',').map(v => v.trim());
    return Object.fromEntries(headers.map((h, i) => [h, isNaN(vals[i]) ? vals[i] : Number(vals[i])]));
  });
}

// Usage
const csv = `Category,Value
Sales,120
Marketing,85
Engineering,200`;

const data = parseCSV(csv);
// => [{ Category: 'Sales', Value: 120 }, ...]
```

### Converting User Data Description to Chart Config

When users describe data in natural language, map it to chart config:

```javascript
// User says: "Show quarterly revenue: Q1 $12M, Q2 $19M, Q3 $8M, Q4 $15M"
// AI generates:
const chartData = {
  labels: ['Q1', 'Q2', 'Q3', 'Q4'],
  datasets: [{
    label: 'Revenue ($M)',
    data: [12, 19, 8, 15],
    backgroundColor: '#0077BB'
  }]
};
```

Pattern: Extract labels from keys/categories, extract numeric values, choose chart type based on data shape:
- Categories + single values = bar chart
- Time series = line chart
- Parts of a whole = pie/doughnut
- Two numeric axes = scatter
- Multi-dimensional comparison = radar
