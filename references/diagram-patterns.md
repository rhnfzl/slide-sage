# Diagram System Reference

Three-tier system for architectural and technical diagrams, ordered by token efficiency.

---

## Tier 0: CSS/HTML Diagrams (Preferred)

Use CSS/HTML diagrams for 80% of diagram needs. They render at full size, respect the theme, and have zero sizing issues. Classes are defined in `assets/viewport-base.css`.

### Sequence/Flow Diagram

Replaces Mermaid sequence diagrams. Uses `.sequence-flow` layout with step rows.

```html
<div class="sequence-flow">
  <div class="seq-participants">
    <div class="seq-actor">User</div>
    <div class="seq-actor">Django</div>
    <div class="seq-actor accent">FastAPI</div>
    <div class="seq-actor">Agent</div>
    <div class="seq-actor">MCP Server</div>
  </div>
  <div class="seq-step">
    <span class="seq-from">User</span>
    <span class="seq-arrow">&rarr;</span>
    <span class="seq-to">Django</span>
    <span class="seq-label">"Find Python devs"</span>
  </div>
  <div class="seq-step">
    <span class="seq-from">Django</span>
    <span class="seq-arrow">&rarr;</span>
    <span class="seq-to">FastAPI</span>
    <span class="seq-label">POST /chat/send + creds</span>
  </div>
  <div class="seq-step">
    <span class="seq-from">FastAPI</span>
    <span class="seq-arrow">&rarr;</span>
    <span class="seq-to">Agent</span>
    <span class="seq-label">run_agent_stream()</span>
  </div>
  <div class="seq-step">
    <span class="seq-from">Agent</span>
    <span class="seq-arrow">&rarr;</span>
    <span class="seq-to">MCP Server</span>
    <span class="seq-label">talent_search(skills=Python)</span>
  </div>
  <div class="seq-step response dashed">
    <span class="seq-from">MCP Server</span>
    <span class="seq-arrow">&larr;</span>
    <span class="seq-to">Agent</span>
    <span class="seq-label">Results (12 candidates)</span>
  </div>
  <div class="seq-step response dashed">
    <span class="seq-from">FastAPI</span>
    <span class="seq-arrow">&larr;</span>
    <span class="seq-to">User</span>
    <span class="seq-label">SSE: streaming response</span>
  </div>
</div>
```

Customize by:
- Adding/removing `.seq-actor` elements for participants
- Using `.accent` class on key participants
- Adding `.response` and `.dashed` classes for return arrows
- Using `&rarr;` for requests and `&larr;` for responses

### Architecture Stack

Replaces inline SVG architecture stacks. Uses `.arch-stack` with rows and groups.

```html
<div class="arch-stack">
  <div class="arch-row full muted">CLIENT LAYER  -  React Frontend</div>
  <div class="arch-row full muted">TM BACKEND  -  Django (Auth, Credentials, History)</div>
  <div class="arch-row full"><span class="badge">01</span> API &amp; Streaming Layer (FastAPI, SSE)</div>
  <div class="arch-row full"><span class="badge badge-gold">02</span> Agent Orchestration (Pydantic AI)</div>
  <div class="arch-row-group">
    <div class="arch-row"><span class="badge">03</span> MCP Client</div>
    <div class="arch-row"><span class="badge">04</span> LLM Provider</div>
    <div class="arch-row"><span class="badge">05</span> Guardrails</div>
  </div>
  <div class="arch-row full"><span class="badge">06</span> Conversation Storage</div>
  <div class="arch-row full"><span class="badge">07</span> Observability</div>
</div>
```

Customize by:
- Using `.muted` for background/context layers
- Using `.arch-row-group` for side-by-side segments
- Using `.badge` and `.badge-gold` for segment numbers

### Pyramid / Hierarchy

Replaces SVG polygon pyramids. Uses `.pyramid` with decreasing widths.

```html
<div class="pyramid">
  <div class="pyramid-layer" style="--width: 35%; border-color: var(--color-text-muted);">
    <strong>LLM-as-Judge</strong>
    <br><small>Pre-release</small>
  </div>
  <div class="pyramid-layer" style="--width: 60%; border-color: var(--color-gold, #D4B02A);">
    <strong style="color: var(--color-gold, #D4B02A);">Agent Trajectory Tests</strong>
    <br><small>Nightly &middot; DeepEval &middot; 50 golden cases</small>
  </div>
  <div class="pyramid-layer" style="--width: 85%; border-color: var(--color-accent);">
    <strong style="color: var(--color-accent);">Deterministic Unit Tests</strong>
    <br><small>Every PR &middot; Tool routing, guardrails, prompt assembly</small>
  </div>
</div>
```

Customize by:
- Setting `--width` per layer (narrowest at top)
- Using `border-color` to color-code layers
- Adding `<strong>` for layer names and `<small>` for details

### Process Flow (Horizontal)

For step-by-step processes, timelines, and pipelines.

```html
<div class="process-flow">
  <div class="process-step">
    <div class="badge">1</div>
    <strong>Ingest</strong>
    <small>Raw data sources</small>
  </div>
  <div class="process-arrow">&rarr;</div>
  <div class="process-step">
    <div class="badge">2</div>
    <strong>Transform</strong>
    <small>Clean &amp; normalize</small>
  </div>
  <div class="process-arrow">&rarr;</div>
  <div class="process-step">
    <div class="badge">3</div>
    <strong>Store</strong>
    <small>Feature store</small>
  </div>
  <div class="process-arrow">&rarr;</div>
  <div class="process-step">
    <div class="badge">4</div>
    <strong>Serve</strong>
    <small>API endpoint</small>
  </div>
</div>
```

### Comparison / Split View

For side-by-side comparisons with accent borders.

```html
<div class="grid-2 gap-md">
  <div class="card card-accent">
    <h3>Primary: Responses API</h3>
    <ul>
      <li><strong style="color: var(--color-accent);">GPT-5-mini</strong> on Azure OpenAI</li>
      <li><code class="inline-code">previous_response_id: 'auto'</code></li>
      <li>Server-side conversation state</li>
    </ul>
  </div>
  <div class="card card-gold">
    <h3>Fallback: Chat Completions</h3>
    <ul>
      <li><strong style="color: var(--color-gold, #D4B02A);">GPT-4.1-mini</strong> on Azure</li>
      <li>Full message history resent</li>
      <li>Automatic failover via Pydantic AI</li>
    </ul>
  </div>
</div>
```

### When to Use CSS/HTML vs Other Tiers

| Diagram Type | Use CSS/HTML | Use SVG Template | Use Inline SVG |
|---|---|---|---|
| Sequence/message flow | Yes (`.sequence-flow`) | - | - |
| Architecture stack | Yes (`.arch-stack`) | - | - |
| Pyramid/hierarchy | Yes (`.pyramid`) | `pyramid-roadmap.svg` | - |
| Process pipeline | Yes (`.process-flow`) | `data-pipeline.svg` | - |
| Comparison/split | Yes (`.grid-2` + `.card`) | - | - |
| Microservices | - | `microservices.svg` | - |
| Network topology | - | `network-zones.svg` | Complex custom |
| Custom shapes | - | - | Yes |
| Hub and spoke | - | `hub-and-spoke.svg` | - |

---

## file:// Protocol Warning (SVG Loading)

Slide-sage presentations are self-contained HTML files viewed locally via `file://` protocol. This imposes restrictions on how SVG assets are loaded.

| Asset Type | `<img src="...">` on `file://` | Recommendation |
|---|---|---|
| Raster images (PNG, JPG, WebP) | Works fine | Use `<img src="assets/photo.png">` |
| SVG diagrams | **Fails silently** in Chrome/Safari | Inline the SVG directly into HTML |
| SVG logos | **Fails silently** | Inline or convert to PNG first |

**Why:** Chrome and Safari block `<img src="local.svg">` on `file://` protocol due to same-origin security policies. The image renders as a broken icon with no console error - a silent failure that's easy to miss.

**Correct patterns:**

```html
<!-- WRONG: broken on file:// -->
<div class="diagram-container">
  <img src="assets/pipeline.svg" alt="Pipeline">
</div>

<!-- CORRECT: inline SVG renders everywhere -->
<div class="diagram-container">
  <svg viewBox="0 0 960 700" xmlns="http://www.w3.org/2000/svg">
    <!-- SVG content directly here -->
  </svg>
</div>

<!-- ALSO CORRECT: <object> tag (works on file://) -->
<object data="templates/diagrams/microservices.svg"
        type="image/svg+xml" style="width:100%;"></object>
```

This warning does NOT apply to CSS/HTML diagrams (Tier 0) or SVG templates loaded via `<object>` (Tier 1) - only to `<img src="*.svg">`.

---

## Tier 1: SVG Templates (Most Token-Efficient)

### Concept

Pre-designed SVG structures live in `templates/diagrams/`. The AI writes only a small JavaScript data object (~200-400 characters) to populate the template. A lightweight renderer reads the data and fills SVG text elements / attributes by ID.

This is the most token-efficient approach: instead of generating 100+ lines of SVG, the AI emits ~5-10 lines of JSON-like data.

### Data Format by Template

#### Microservices (`microservices.svg`)

```javascript
const diagram = {
  type: 'microservices',
  gateway: 'API Gateway',
  services: [
    { name: 'Auth Service', db: 'PostgreSQL', color: 'var(--diagram-primary)' },
    { name: 'Order Service', db: 'MongoDB', color: 'var(--diagram-secondary)' },
    { name: 'Payment Service', db: 'Redis', color: 'var(--diagram-amber)' }
  ]
};
```

#### Data Pipeline (`data-pipeline.svg`)

```javascript
const diagram = {
  type: 'pipeline',
  nodes: [
    { name: 'Ingest', icon: 'db' },
    { name: 'Transform', icon: 'gear' },
    { name: 'Validate', icon: 'check' },
    { name: 'Store', icon: 'db' }
  ]
};
```

#### Client-Server (`client-server.svg`)

```javascript
const diagram = {
  type: 'client-server',
  clients: [{ name: 'Web App' }, { name: 'Mobile App' }],
  server: { name: 'API Server' },
  database: { name: 'PostgreSQL' },
  labels: { request: 'REST API', response: 'JSON' }
};
```

#### Layered Architecture (`layered-arch.svg`)

```javascript
const diagram = {
  type: 'layered',
  layers: [
    { name: 'Presentation', items: ['React SPA', 'Admin Dashboard'] },
    { name: 'Business Logic', items: ['Auth Service', 'Order Engine', 'Analytics'] },
    { name: 'Data Layer', items: ['PostgreSQL', 'Redis Cache', 'S3 Storage'] }
  ]
};
```

#### CI/CD Pipeline (`cicd-pipeline.svg`)

```javascript
const diagram = {
  type: 'cicd-pipeline',
  stages: [
    { name: 'Code', status: 'passed' },
    { name: 'Build', status: 'passed' },
    { name: 'Test', status: 'running' },
    { name: 'Stage', status: 'pending' },
    { name: 'Deploy', status: 'pending' }
  ],
  showRollback: false
};
```

#### Hub and Spoke (`hub-and-spoke.svg`)

```javascript
const diagram = {
  type: 'hub-spoke',
  hub: 'Platform Core',
  spokes: [
    { name: 'Auth Service', arrow: 'gRPC' },
    { name: 'Search', arrow: 'REST' },
    { name: 'Analytics', arrow: 'Events' },
    { name: 'Billing', arrow: 'REST' },
    { name: 'Notifications', arrow: 'Pub/Sub' },
    { name: 'Storage', arrow: 'S3 API' }
  ]
};
```

#### Cloud Three-Tier (`cloud-three-tier.svg`)

```javascript
const diagram = {
  type: 'cloud-three-tier',
  zones: [
    { name: 'Internet' },
    { name: 'Load Balancing' },
    { name: 'Application' },
    { name: 'Database' }
  ],
  apps: ['API Server', 'Worker'],
  dbs: ['PostgreSQL']
};
```

#### Kubernetes Cluster (`kubernetes-cluster.svg`)

```javascript
const diagram = {
  type: 'kubernetes',
  cluster: 'Production',
  controlPlane: ['API Server', 'Scheduler', 'Controller Mgr', 'etcd'],
  workers: [
    { name: 'Worker 1', pods: ['nginx', 'app'] },
    { name: 'Worker 2', pods: ['cache', 'api'] }
  ]
};
```

#### Event-Driven Pub/Sub (`event-driven-pubsub.svg`)

```javascript
const diagram = {
  type: 'event-pubsub',
  publishers: ['Order Service', 'User Service', 'Payment Service'],
  bus: 'Event Bus',
  topics: ['orders', 'users', 'payments'],
  subscribers: ['Analytics', 'Notifications', 'Audit Log']
};
```

#### ML Pipeline (`ml-pipeline.svg`)

```javascript
const diagram = {
  type: 'ml-pipeline',
  sources: ['Clickstream', 'User DB', 'Product DB'],
  features: ['Embeddings', 'Aggregations', 'Transforms'],
  store: 'Feature Store',
  training: ['Preprocessing', 'Training', 'Evaluation'],
  registry: 'Model Registry',
  serving: ['API Server', 'Batch Scorer']
};
```

#### C4 System Context (`c4-context.svg`)

```javascript
const diagram = {
  type: 'c4-context',
  system: { name: 'E-Commerce Platform', desc: 'Handles orders and payments' },
  persons: [
    { name: 'Customer', desc: 'Places orders' }
  ],
  externals: [
    { name: 'Payment Gateway', desc: 'Processes payments' },
    { name: 'Email Service', desc: 'Sends notifications' }
  ]
};
```

#### Network/Security Zones (`network-zones.svg`)

```javascript
const diagram = {
  type: 'network-zones',
  zones: [
    { name: 'Internet', services: ['CDN', 'WAF'] },
    { name: 'DMZ', services: ['API Gateway', 'Auth Proxy'] },
    { name: 'Internal', services: ['App Server', 'Database'] }
  ],
  firewalls: ['Edge Firewall', 'Internal Firewall']
};
```

#### API Gateway + Auth (`api-gateway-auth.svg`)

```javascript
const diagram = {
  type: 'api-gateway-auth',
  client: 'Client App',
  gateway: 'API Gateway',
  auth: 'Auth Service',
  token: 'JWT Token',
  services: ['Users API', 'Orders API', 'Products API']
};
```

#### Pyramid/Roadmap (`pyramid-roadmap.svg`)

```javascript
const diagram = {
  type: 'pyramid-roadmap',
  levels: [
    { name: 'Foundation', status: 'Complete' },
    { name: 'Core Platform', status: 'Complete' },
    { name: 'Integrations', status: 'In Progress' },
    { name: 'Advanced Features', status: 'Planned' },
    { name: 'AI/ML Layer', status: 'Future' }
  ],
  axis: 'Maturity'
};
```

#### Funnel (`funnel.svg`)

```javascript
const diagram = {
  type: 'funnel',
  stages: [
    { name: 'Visitors', value: '10,000' },
    { name: 'Signups', value: '2,500' },
    { name: 'Active Users', value: '1,200' },
    { name: 'Paid Users', value: '450' }
  ],
  conversions: ['25%', '48%', '37.5%']
};
```

#### Nested Scopes (`nested-scopes.svg`)

```javascript
const diagram = {
  type: 'nested-scopes',
  scopes: [
    { name: 'Organization' },
    { name: 'Team' },
    { name: 'Project' }
  ],
  items: ['Service A', 'Service B', 'Service C']
};
```

#### Tree Hierarchy (`tree-hierarchy.svg`)

```javascript
const diagram = {
  type: 'tree-hierarchy',
  root: 'Platform',
  branches: [
    { name: 'Frontend', leaves: ['React App', 'Mobile App'] },
    { name: 'Backend', leaves: ['API Service', 'Worker Service'] }
  ]
};
```

### Template Renderer

Place this in the slide's `<script>` block after the data object. It populates text elements by their IDs.

```javascript
function renderDiagram(svgId, data) {
  const svg = document.getElementById(svgId);
  if (!svg) return;

  if (data.type === 'microservices') {
    setText(svg, 'gateway-label', data.gateway);
    data.services.forEach((svc, i) => {
      const n = i + 1;
      setText(svg, `svc-${n}-label`, svc.name);
      setText(svg, `svc-${n}-db-label`, svc.db || '');
      setAttr(svg, `svc-${n}-box`, 'fill', svc.color || 'var(--diagram-primary)');
      toggle(svg, `svc-${n}-group`, true);
      toggle(svg, `svc-${n}-db-group`, !!svc.db);
    });
    // Hide unused service slots
    for (let i = data.services.length + 1; i <= 5; i++) {
      toggle(svg, `svc-${i}-group`, false);
      toggle(svg, `svc-${i}-db-group`, false);
    }
  } else if (data.type === 'pipeline') {
    data.nodes.forEach((node, i) => {
      setText(svg, `node-${i + 1}-label`, node.name);
      toggle(svg, `node-${i + 1}-group`, true);
    });
    for (let i = data.nodes.length + 1; i <= 6; i++) {
      toggle(svg, `node-${i}-group`, false);
    }
  } else if (data.type === 'client-server') {
    setText(svg, 'server-label', data.server.name);
    setText(svg, 'db-label', data.database?.name || '');
    setText(svg, 'request-label', data.labels?.request || '');
    setText(svg, 'response-label', data.labels?.response || '');
    data.clients.forEach((c, i) => setText(svg, `client-${i + 1}-label`, c.name));
  } else if (data.type === 'layered') {
    data.layers.forEach((layer, i) => {
      const n = i + 1;
      setText(svg, `layer-${n}-name`, layer.name);
      layer.items.forEach((item, j) => setText(svg, `layer-${n}-item-${j + 1}`, item));
    });
  } else if (data.type === 'cicd-pipeline') {
    data.stages.forEach((stage, i) => {
      const n = i + 1;
      setText(svg, `stage-${n}-label`, stage.name);
      setAttr(svg, `stage-${n}-box`, 'class', `stage stage-${stage.status}`);
      toggle(svg, `stage-${n}-group`, true);
    });
    for (let i = data.stages.length + 1; i <= 6; i++) {
      toggle(svg, `stage-${i}-group`, false);
    }
    toggle(svg, 'rollback-group', !!data.showRollback);
  } else if (data.type === 'hub-spoke') {
    setText(svg, 'hub-label', data.hub);
    data.spokes.forEach((spoke, i) => {
      const n = i + 1;
      setText(svg, `spoke-${n}-label`, spoke.name);
      setText(svg, `spoke-${n}-arrow-label`, spoke.arrow || '');
      toggle(svg, `spoke-${n}-group`, true);
    });
    for (let i = data.spokes.length + 1; i <= 8; i++) {
      toggle(svg, `spoke-${i}-group`, false);
    }
  } else if (data.type === 'cloud-three-tier') {
    data.zones.forEach((zone, i) => {
      const n = i + 1;
      setText(svg, `zone-${n}-label`, zone.name);
      toggle(svg, `zone-${n}-group`, true);
    });
    for (let i = data.zones.length + 1; i <= 5; i++) {
      toggle(svg, `zone-${i}-group`, false);
    }
    data.apps.forEach((app, i) => {
      setText(svg, `app-${i + 1}-label`, app);
      toggle(svg, `app-${i + 1}-group`, true);
    });
    for (let i = data.apps.length + 1; i <= 3; i++) {
      toggle(svg, `app-${i}-group`, false);
    }
    data.dbs.forEach((db, i) => {
      setText(svg, `db-${i + 1}-label`, db);
      toggle(svg, `db-${i + 1}-group`, true);
    });
    for (let i = data.dbs.length + 1; i <= 2; i++) {
      toggle(svg, `db-${i}-group`, false);
    }
  } else if (data.type === 'kubernetes') {
    setText(svg, 'cluster-label', data.cluster);
    data.controlPlane.forEach((cp, i) => {
      setText(svg, `cp-${i + 1}-label`, cp);
      toggle(svg, `cp-${i + 1}-group`, true);
    });
    data.workers.forEach((worker, i) => {
      const n = i + 1;
      setText(svg, `worker-${n}-label`, worker.name);
      toggle(svg, `worker-${n}-group`, true);
      worker.pods.forEach((pod, j) => {
        setText(svg, `worker-${n}-pod-${j + 1}-label`, pod);
        toggle(svg, `worker-${n}-pod-${j + 1}-group`, true);
      });
      for (let j = worker.pods.length + 1; j <= 3; j++) {
        toggle(svg, `worker-${n}-pod-${j}-group`, false);
      }
    });
  } else if (data.type === 'event-pubsub') {
    setText(svg, 'bus-label', data.bus);
    data.publishers.forEach((pub, i) => {
      const n = i + 1;
      setText(svg, `pub-${n}-label`, pub);
      toggle(svg, `pub-${n}-group`, true);
    });
    for (let i = data.publishers.length + 1; i <= 4; i++) {
      toggle(svg, `pub-${i}-group`, false);
    }
    data.topics.forEach((topic, i) => setText(svg, `topic-${i + 1}-label`, topic));
    data.subscribers.forEach((sub, i) => {
      const n = i + 1;
      setText(svg, `sub-${n}-label`, sub);
      toggle(svg, `sub-${n}-group`, true);
    });
    for (let i = data.subscribers.length + 1; i <= 4; i++) {
      toggle(svg, `sub-${i}-group`, false);
    }
  } else if (data.type === 'ml-pipeline') {
    data.sources.forEach((src, i) => setText(svg, `source-${i + 1}-label`, src));
    data.features.forEach((feat, i) => setText(svg, `feature-${i + 1}-label`, feat));
    setText(svg, 'store-label', data.store);
    data.training.forEach((step, i) => setText(svg, `train-${i + 1}-label`, step));
    setText(svg, 'registry-label', data.registry);
    data.serving.forEach((svc, i) => setText(svg, `serve-${i + 1}-label`, svc));
  } else if (data.type === 'c4-context') {
    setText(svg, 'system-label', data.system.name);
    setText(svg, 'system-desc', data.system.desc);
    data.persons.forEach((p, i) => {
      const n = i + 1;
      setText(svg, `person-${n}-label`, p.name);
      setText(svg, `person-${n}-desc`, p.desc);
      toggle(svg, `person-${n}-group`, true);
    });
    for (let i = data.persons.length + 1; i <= 2; i++) {
      toggle(svg, `person-${i}-group`, false);
    }
    data.externals.forEach((ext, i) => {
      const n = i + 1;
      setText(svg, `ext-${n}-label`, ext.name);
      setText(svg, `ext-${n}-desc`, ext.desc);
      toggle(svg, `ext-${n}-group`, true);
    });
    for (let i = data.externals.length + 1; i <= 3; i++) {
      toggle(svg, `ext-${i}-group`, false);
    }
  } else if (data.type === 'network-zones') {
    data.zones.forEach((zone, i) => {
      const n = i + 1;
      setText(svg, `zone-${n}-label`, zone.name);
      toggle(svg, `zone-${n}-group`, true);
      zone.services.forEach((svc, j) => {
        setText(svg, `zone-${n}-svc-${j + 1}-label`, svc);
        toggle(svg, `zone-${n}-svc-${j + 1}-group`, true);
      });
      for (let j = zone.services.length + 1; j <= 3; j++) {
        toggle(svg, `zone-${n}-svc-${j}-group`, false);
      }
    });
    data.firewalls.forEach((fw, i) => setText(svg, `firewall-${i + 1}-label`, fw));
  } else if (data.type === 'api-gateway-auth') {
    setText(svg, 'client-label', data.client);
    setText(svg, 'gateway-label', data.gateway);
    setText(svg, 'auth-label', data.auth);
    setText(svg, 'token-label', data.token);
    data.services.forEach((svc, i) => {
      const n = i + 1;
      setText(svg, `backend-${n}-label`, svc);
      toggle(svg, `backend-${n}-group`, true);
    });
    for (let i = data.services.length + 1; i <= 4; i++) {
      toggle(svg, `backend-${i}-group`, false);
    }
  } else if (data.type === 'pyramid-roadmap') {
    data.levels.forEach((level, i) => {
      const n = i + 1;
      setText(svg, `level-${n}-label`, level.name);
      setText(svg, `level-${n}-status`, level.status || '');
      toggle(svg, `level-${n}-group`, true);
    });
    for (let i = data.levels.length + 1; i <= 6; i++) {
      toggle(svg, `level-${i}-group`, false);
    }
    if (data.axis) setText(svg, 'axis-label', data.axis);
  } else if (data.type === 'funnel') {
    data.stages.forEach((stage, i) => {
      const n = i + 1;
      setText(svg, `funnel-${n}-label`, stage.name);
      setText(svg, `funnel-${n}-value`, stage.value);
      toggle(svg, `funnel-${n}-group`, true);
    });
    for (let i = data.stages.length + 1; i <= 5; i++) {
      toggle(svg, `funnel-${i}-group`, false);
    }
    if (data.conversions) {
      data.conversions.forEach((conv, i) => setText(svg, `conv-${i + 1}-label`, conv));
    }
  } else if (data.type === 'nested-scopes') {
    data.scopes.forEach((scope, i) => {
      const n = i + 1;
      setText(svg, `scope-${n}-label`, scope.name);
      toggle(svg, `scope-${n}-group`, true);
    });
    for (let i = data.scopes.length + 1; i <= 4; i++) {
      toggle(svg, `scope-${i}-group`, false);
    }
    data.items.forEach((item, i) => {
      setText(svg, `item-${i + 1}-label`, item);
      toggle(svg, `item-${i + 1}-group`, true);
    });
  } else if (data.type === 'tree-hierarchy') {
    setText(svg, 'root-label', data.root);
    data.branches.forEach((branch, i) => {
      const n = i + 1;
      setText(svg, `branch-${n}-label`, branch.name);
      toggle(svg, `branch-${n}-group`, true);
      branch.leaves.forEach((leaf, j) => {
        setText(svg, `branch-${n}-leaf-${j + 1}-label`, leaf);
        toggle(svg, `branch-${n}-leaf-${j + 1}-group`, true);
      });
      for (let j = branch.leaves.length + 1; j <= 3; j++) {
        toggle(svg, `branch-${n}-leaf-${j}-group`, false);
      }
    });
    for (let i = data.branches.length + 1; i <= 3; i++) {
      toggle(svg, `branch-${i}-group`, false);
    }
  }

  function setText(root, id, text) {
    const el = root.querySelector(`#${id}`);
    if (el) el.textContent = text;
  }
  function setAttr(root, id, attr, val) {
    const el = root.querySelector(`#${id}`);
    if (el) el.setAttribute(attr, val);
  }
  function toggle(root, id, show) {
    const el = root.querySelector(`#${id}`);
    if (el) el.style.display = show ? '' : 'none';
  }
}
```

### Template Catalog

| Template | File | Type | Default Slots | Hidden Slots | Best For |
|----------|------|------|---------------|--------------|----------|
| Microservices | microservices.svg | Architecture | 3 services | +2 | Service mesh, API-first |
| Data Pipeline | data-pipeline.svg | Architecture | 4 nodes | +2 | ETL, data flow |
| Client-Server | client-server.svg | Architecture | 2 clients + 1 server | - | Simple request/response |
| Layered Architecture | layered-arch.svg | Architecture | 3 layers x 3 items | - | N-tier, clean arch |
| CI/CD Pipeline | cicd-pipeline.svg | DevOps | 5 stages | +1 | Build/deploy pipelines |
| Hub and Spoke | hub-and-spoke.svg | Platform | 6 spokes | +2 | Central platform |
| Cloud Three-Tier | cloud-three-tier.svg | Cloud | 4 zones | +1 app, +1 db | Cloud architecture |
| Kubernetes Cluster | kubernetes-cluster.svg | DevOps | 4 CP + 2x2 pods | +1 pod each | K8s deployments |
| Event Pub/Sub | event-driven-pubsub.svg | Backend | 3 pub + 3 sub | +1 each | Event-driven systems |
| ML Pipeline | ml-pipeline.svg | ML/AI | 3 stages | - | ML system design |
| C4 Context | c4-context.svg | Architecture | 1 person + 2 ext | +1 each | System context |
| Network Zones | network-zones.svg | Security | 3 zones x 2 svc | +1 each | Security architecture |
| API Gateway | api-gateway-auth.svg | Backend | 3 backend svc | - | API routing + auth |
| Pyramid/Roadmap | pyramid-roadmap.svg | General | 5 levels | - | Maturity stages |
| Funnel | funnel.svg | General | 4 stages | +1 | Conversion flows |
| Nested Scopes | nested-scopes.svg | General | 3 scopes | +1 | Containment hierarchy |
| Tree Hierarchy | tree-hierarchy.svg | General | 2 branches x 2 leaves | +1 branch | Org charts, taxonomies |

### Embedding in a Slide

```html
<div class="diagram-container" style="max-height:min(60vh,450px); width:100%; display:flex; justify-content:center;">
  <object id="arch-diagram" data="templates/diagrams/microservices.svg"
          type="image/svg+xml" style="width:100%; max-height:inherit;"></object>
</div>
<script>
document.getElementById('arch-diagram').addEventListener('load', function() {
  const svgDoc = this.contentDocument;
  renderDiagram(svgDoc.querySelector('svg').id || svgDoc.documentElement, {
    type: 'microservices',
    gateway: 'API Gateway',
    services: [
      { name: 'User Service', db: 'PostgreSQL', color: 'var(--diagram-primary)' },
      { name: 'Order Service', db: 'DynamoDB', color: 'var(--diagram-secondary)' }
    ]
  });
});
</script>
```

### Inline SVG Alternative

For single-file presentations, inline the SVG directly instead of using `<object>`:

```html
<div class="diagram-container" style="max-height:min(60vh,450px); width:100%;">
  <!-- paste SVG content here, or use fetch -->
</div>
```

### Hand-Drawn Variant with Rough.js

Add a sketch/whiteboard aesthetic using Rough.js (~9KB gzipped). Replace clean SVG shapes with hand-drawn equivalents.

```html
<script src="https://cdn.jsdelivr.net/npm/roughjs@4.6.6/bundled/rough.min.js"></script>
<script>
function sketchify(svgElement) {
  const rc = rough.svg(svgElement);
  // Replace each <rect> with a rough rectangle
  svgElement.querySelectorAll('rect[data-sketch]').forEach(rect => {
    const x = +rect.getAttribute('x'), y = +rect.getAttribute('y');
    const w = +rect.getAttribute('width'), h = +rect.getAttribute('height');
    const fill = rect.getAttribute('fill') || 'var(--diagram-primary, #0077BB)';
    const roughRect = rc.rectangle(x, y, w, h, {
      fill, fillStyle: 'hachure', roughness: 1.5, strokeWidth: 1.5, stroke: '#333'
    });
    rect.parentNode.replaceChild(roughRect, rect);
  });
  // Replace each <line> with a rough line
  svgElement.querySelectorAll('line[data-sketch]').forEach(line => {
    const x1 = +line.getAttribute('x1'), y1 = +line.getAttribute('y1');
    const x2 = +line.getAttribute('x2'), y2 = +line.getAttribute('y2');
    const roughLine = rc.line(x1, y1, x2, y2, { roughness: 1.2, strokeWidth: 1.5 });
    line.parentNode.replaceChild(roughLine, line);
  });
}
</script>
```

Add `data-sketch` attribute to SVG elements you want to convert.

---

## Tier 3: Inline SVG (Fully Custom)

For diagrams that need precise positioning, custom shapes, or interactive elements. **Always inline SVGs** directly in the HTML - never use `<img src="file.svg">` (see file:// Protocol Warning above).

### Responsive viewBox Pattern

```html
<svg viewBox="0 0 800 500" preserveAspectRatio="xMidYMid meet"
     style="width:100%; max-height:min(60vh,450px);" xmlns="http://www.w3.org/2000/svg">
  <!-- diagram content -->
</svg>
```

### viewBox Aspect Ratio

For full-slide diagrams, **prefer a taller ratio** (e.g., `viewBox="0 0 900 860"`) over wide-and-short (e.g., `0 0 1100 750`). Wide viewBoxes render tiny on widescreen monitors because the height becomes the limiting dimension.

| Diagram Shape | Recommended viewBox | Use Case |
|---|---|---|
| Tall/portrait | `0 0 900 860` | Architecture stacks, layered systems |
| Square | `0 0 800 800` | Hub-and-spoke, radial layouts |
| Landscape | `0 0 960 600` | Sequence flows, timelines |
| Wide | `0 0 1100 500` | Only for horizontal pipelines |

### SVG Font Sizing

SVG text scales with the viewBox, so it appears **smaller** than HTML text at the same nominal size. Use these minimums:

| Content | Minimum `font-size` |
|---|---|
| Body text / descriptions | 14px |
| Component labels | 16-18px |
| Section headings inside SVG | 19-22px |

### Glow Highlights

Use `<filter>` with `feGaussianBlur` to create glow effects on key components (e.g., the new technology being introduced):

```xml
<defs>
  <filter id="glow-accent" x="-20%" y="-20%" width="140%" height="140%">
    <feGaussianBlur in="SourceGraphic" stdDeviation="6" result="blur"/>
    <feMerge>
      <feMergeNode in="blur"/>
      <feMergeNode in="SourceGraphic"/>
    </feMerge>
  </filter>
</defs>

<!-- Apply to a key component -->
<rect x="100" y="200" width="180" height="70" rx="10"
      fill="var(--diagram-primary)" filter="url(#glow-accent)"/>
```

### Full-Slide Diagram Container

When a diagram needs maximum space, reduce slide padding and expand the container:

```html
<div class="slide" style="padding: clamp(0.3rem, 1vw, 1rem);">
  <div class="slide-content" style="justify-content: center; gap: 0;">
    <div style="width: 100%; max-width: 1200px; margin: 0 auto;">
      <svg viewBox="0 0 900 860" xmlns="http://www.w3.org/2000/svg"
           style="width: 100%; height: auto; max-height: 96vh;">
        <defs><!-- markers, filters --></defs>
        <!-- diagram content -->
      </svg>
    </div>
  </div>
</div>
```

### Color Matching

Use the same CSS custom properties as the surrounding slides for diagram colors:

- Text: `var(--color-text-primary)`, `var(--color-text-muted)`
- Accents: `var(--color-accent)`, `var(--color-gold, #D4B02A)`
- Borders: `var(--color-border)`
- Arrow fills: `var(--diagram-arrow, #888)`

### Arrowhead Marker Definition

Use this generic marker only when every directional line uses the same default arrow color. When a diagram uses more than one stroke color, define one marker per color as required by Rule 3.

Include once in `<defs>`:

```xml
<defs>
  <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
    <polygon points="0 0, 10 3.5, 0 7" fill="var(--diagram-arrow, #888)" />
  </marker>
  <marker id="arrowhead-reverse" markerWidth="10" markerHeight="7" refX="0" refY="3.5" orient="auto">
    <polygon points="10 0, 0 3.5, 10 7" fill="var(--diagram-arrow, #888)" />
  </marker>
</defs>
```

---

## SVG Diagram Construction Rules (HARD RULES)

These rules prevent the most common SVG diagram bugs in presentations. Every rule was learned from real rendering failures - follow them exactly.

### Rule 1: Always Center Text Inside Boxes (NON-NEGOTIABLE)

**NEVER** position `<text>` with a left-offset `x` inside a `<rect>`. SVG text defaults to `text-anchor="start"` (left-aligned), which looks misaligned inside centered boxes.

**Always use:**
```xml
<rect x="30" y="10" width="180" height="50" rx="8" .../>
<text x="120" y="40" text-anchor="middle" ...>Label</text>
<!--       ^ x = rect_x + rect_width / 2 -->
```

**Formula:** `text_x = rect_x + (rect_width / 2)`

This applies to ALL text inside ALL rect boxes - titles, subtitles, descriptions, code labels. No exceptions.

**Multi-line text inside a box:**
```xml
<rect x="185" y="20" width="170" height="85" rx="6" .../>
<!-- All lines share the same centered x -->
<text x="270" y="45" text-anchor="middle" font-weight="600">Title</text>
<text x="270" y="65" text-anchor="middle">Line 1</text>
<text x="270" y="80" text-anchor="middle">Line 2</text>
```

### Rule 2: viewBox Must Encompass All Elements + Margin

SVG silently clips anything outside the viewBox. There is no overflow, no error, no warning - content just disappears.

**Before finalizing any SVG:**
1. Find the lowest `y + height` of any `<rect>` or the highest `y` of any `<text>`
2. Find the rightmost `x + width`
3. Set viewBox height = max_y + **15px margin**
4. Set viewBox width = max_x + **15px margin**

**Common failure:** A box at `y="76" height="30"` in a `viewBox="0 0 700 100"` - bottom 6px is clipped.

**Fix:** `viewBox="0 0 700 120"` (or use negative origin `viewBox="0 -5 800 130"` if elements go above y=0).

### Rule 3: One Arrow Marker Per Color

Each arrow color needs its own `<marker>` definition in `<defs>`. You cannot reuse a green marker for a red arrow - the arrowhead will render green regardless of the line's `stroke` color.

```xml
<defs>
    <marker id="arr-green" viewBox="0 0 10 10" refX="8" refY="5"
            markerWidth="6" markerHeight="6" orient="auto">
        <path d="M0,0 L10,5 L0,10 Z" fill="#00ff88"/>
    </marker>
    <marker id="arr-red" viewBox="0 0 10 10" refX="8" refY="5"
            markerWidth="6" markerHeight="6" orient="auto">
        <path d="M0,0 L10,5 L0,10 Z" fill="#ef4444"/>
    </marker>
    <marker id="arr-gray" viewBox="0 0 10 10" refX="8" refY="5"
            markerWidth="6" markerHeight="6" orient="auto">
        <path d="M0,0 L10,5 L0,10 Z" fill="#64748b"/>
    </marker>
</defs>
```

**Every `<line>` with `marker-end` must reference the marker matching its stroke color.** Dashed lines (e.g., error/fallback paths) need arrowheads too - don't omit `marker-end` just because the line is dashed.

### Rule 4: Arrow and Line Color Contrast

**NEVER** use colors close to the slide background for arrows or connecting lines. On dark backgrounds (`#0d1425`, `#0a0f1c`), these are invisible:

| Color | Visible on dark? | Use instead |
|-------|-------------------|-------------|
| `#1e293b` | **NO** - nearly same as background | `#64748b` (muted gray) |
| `#0f172a` | **NO** | `#475569` or `#64748b` |
| `#334155` | Barely | `#64748b` minimum |

**Safe minimum contrast colors for dark backgrounds:** `#64748b` (gray), `#94a3b8` (light gray), or any accent color.

### Rule 5: Center Arrow Labels at Midpoints

Labels on arrows between boxes should be centered at the arrow's midpoint, not left-aligned from the arrow start.

```xml
<!-- Arrow from box1 (ends at x=230) to box2 (starts at x=280) -->
<line x1="230" y1="90" x2="280" y2="90" stroke="#00ff88" .../>
<!-- Label at midpoint: (230+280)/2 = 255 -->
<text x="255" y="82" text-anchor="middle" ...>HTTP</text>
```

### Rule 6: Two-Column Text in SVG Containers

When a wide SVG box has two content columns:

1. **Calculate the box center:** `center_x = box_x + box_width / 2`
2. **Place columns symmetrically:** `col1_x = center_x - offset`, `col2_x = center_x + offset`
3. **Typical offset:** 30-40% of half-width works well

```xml
<!-- Box from x=100, width=580 -> center at 390 -->
<rect x="100" y="170" width="580" height="140" .../>
<text x="390" y="195" text-anchor="middle">TITLE</text>
<!-- Col 1 at ~center - 120 = 270, Col 2 at ~center + 120 = 510 -->
<text x="270" y="220" text-anchor="middle">Col 1 item</text>
<text x="510" y="220" text-anchor="middle">Col 2 item</text>
```

**Warning:** Mathematical symmetry doesn't always look visually symmetric because text widths differ. If the result looks misaligned, adjust by 10-15px toward the wider-text column. The screen is the source of truth.

### Rule 7: Roadmap / Stage Diagrams - Badges vs Titles

When stages have both a badge (step number/phase label) and a title:

- **Badges:** Small (35-50px wide), positioned at the right edge of the stage bar, font-size 7-8
- **Titles:** Centered at the bar's horizontal midpoint (`text-anchor="middle"`), font-size 11-13
- **Descriptions:** Below the title on a separate line, font-size 9-10, muted color

```xml
<!-- Stage bar: x=50, width=700 -> center at 400 -->
<rect x="50" y="20" width="700" height="35" rx="6" .../>
<text x="400" y="42" text-anchor="middle" font-size="12" font-weight="600">Stage Title</text>
<text x="400" y="56" text-anchor="middle" font-size="9" fill="#94a3b8">Description below</text>
<!-- Badge at right edge -->
<rect x="710" y="24" width="35" height="18" rx="4" fill="#3b82f6"/>
<text x="727" y="37" text-anchor="middle" font-size="7" fill="white">BLUE</text>
```

**Never** let badges overlap title text. If the bar is narrow, shrink badges first.

### Rule 8: State Machine Diagrams

For state machine / flow diagrams with loops and terminal states:

1. **Loop-back arrows go ABOVE** the main flow, not below. Use a quadratic Bezier curve:
   ```xml
   <!-- Loop from box at x=350 back to box at x=150 (arc above) -->
   <path d="M350,top Q250,-20 150,top" fill="none" stroke="#fbbf24"
         stroke-width="1.5" marker-end="url(#arr-yellow)"/>
   ```
2. **Terminal states** (cancelled, expired, rejected) branch downward from the main flow
3. **Every branch needs an arrowhead** - including dashed error/timeout paths
4. **Label transitions** on or near the arrow with the trigger event

### Rule 9: Multi-Row Diagrams - Row Centering

When a diagram has multiple horizontal rows of boxes (e.g., main flow on top, schedule flow below):

1. **Add a visual separator** between rows: a text label like "-- OR --" or "Path 2: Schedule-driven"
2. **Center each row independently** - don't assume row 1 alignment applies to row 2
3. **Label each row** with its purpose (e.g., "Path 1: Event-driven" / "Path 2: Schedule-driven")

### Rule 10: Nested Box Diagrams (Memory Hierarchies, Scopes)

For nested rectangles showing containment/scope:

- **Center ALL text within its containing box**, not left-aligned
- Each nesting level: inset 20-30px from parent on each side
- Use `rgba()` fills at low opacity for nesting (e.g., `rgba(59,130,246,0.05)`) so inner boxes show through
- **Title + description** pattern: title in accent color (font-size 12, bold), description in muted color (font-size 9) on the next line

### Rule 11: Pyramid / Triangle Diagrams

For layered pyramids (evaluation tiers, hierarchies):

- Use `<polygon>` for triangle/trapezoid shapes
- **ALL text inside EVERY layer uses `text-anchor="middle"`** with x at the shape's horizontal center
- The horizontal center of a symmetric triangle/trapezoid: `(left_x + right_x) / 2`
- Layer labels: accent color, font-weight 600
- Layer descriptions: muted color, smaller font-size, below the label

### Rule 12: Box Height Must Fit Text Content

When a `<rect>` contains text, ensure the rect height accommodates all lines:

- **Minimum height:** `(number_of_text_lines x line_spacing) + top_padding + bottom_padding`
- Typical line spacing: 15-18px for font-size 9-11
- Typical padding: 10-15px top and bottom
- **A box with 1 line of text** needs at least 30-35px height
- **A box with 3 lines** needs at least 60-70px height

If text appears clipped at the bottom of a box, increase the rect height AND the viewBox height.

### Rule 13: Presentation Title Should Reflect the Whole, Not a Part

> **Note:** This is a general content rule, not SVG-specific. Full guidance with examples in `references/style-guide.md` → "Presentation Title Rule".

The title must represent the **entire scope** of the presentation, not just one subsystem. If the presentation has N major sections and the title only describes one of them, the title is too narrow - pick the umbrella term that covers all sections.

### Rule 14: Dashed Lines Need Minimum Visible Length

A `stroke-dasharray="4 3"` line that's only 13px long shows barely one dash - it looks like a rendering glitch, not a connection.

- **Minimum line length:** 25px between source element and target element
- If the gap between two boxes is too small, shift the target box to create at least 25px of space
- Also increase the viewBox dimensions to accommodate the shifted element

```xml
<!-- BAD: 13px dashed line - barely visible -->
<line x1="375" y1="85" x2="375" y2="98" stroke="#ef4444" stroke-dasharray="3"/>

<!-- GOOD: 25px dashed line - dash pattern clearly visible -->
<line x1="375" y1="85" x2="375" y2="110" stroke="#ef4444" stroke-dasharray="4 3"
      marker-end="url(#arr-red)"/>
```

### Rule 15: Every Directional Line Needs an Arrowhead

Rule 3 says arrowheads must match the line color. This rule goes further: **every line that represents directional flow MUST have `marker-end`**. No exceptions.

Lines without arrowheads look like static borders or decorative separators - not flow connections. This applies to:
- Converging lines (multiple sources merging into one target)
- Branching lines (one source splitting to multiple targets)
- Connecting lines between diagram sections

```xml
<!-- BAD: no arrowhead - looks like a static border -->
<line x1="150" y1="200" x2="150" y2="240" stroke="#00ff88" stroke-width="1.5"/>

<!-- GOOD: arrowhead shows this is a directional flow -->
<line x1="150" y1="200" x2="150" y2="238" stroke="#00ff88" stroke-width="1.5"
      marker-end="url(#arr-green)"/>
```

### Rule 16: Abbreviated Labels Need Sub-Descriptions

Short labels like "B1", "B2", "Phase 1", "Step A" are meaningless without context. Always add a descriptive sub-label below the abbreviation in a smaller, muted font.

```xml
<!-- BAD: "B1" means nothing to the audience -->
<text x="155" y="40" fill="#ef4444" font-size="8" text-anchor="middle">B1</text>

<!-- GOOD: abbreviation + description -->
<text x="155" y="30" fill="#ef4444" font-size="8" text-anchor="middle">B1</text>
<text x="155" y="40" fill="#64748b" font-size="7" text-anchor="middle">Session-JWT</text>
```

For bottom-of-diagram legends, add a summary line:
```xml
<text x="400" y="155" fill="#64748b" font-size="8" text-anchor="middle">
    B1-B4 = Trust boundaries where authentication is enforced
</text>
```

### Rule 17: Inter-Box Gaps Must Fit Label Text

When an arrow between two boxes carries a text label (e.g., "HTTP", "Streamable HTTP"), the gap between the boxes must be wide enough to display the full label.

**Before placing a label:**
1. Estimate the label's pixel width: `char_count x ~7px` for font-size 8-9
2. Add 20px padding on each side
3. If the gap is smaller than `label_width + 40px`, widen the viewBox and shift the downstream box

```xml
<!-- BAD: 55px gap for "Streamable HTTP" (14 chars x 7px = 98px) - truncated -->
<rect x="285" ... width="230"/>  <!-- ends at 515 -->
<rect x="570" .../>              <!-- gap = 55px -->

<!-- GOOD: 145px gap - label fits with the required padding -->
<rect x="290" ... width="220"/>  <!-- ends at 510 -->
<rect x="655" .../>              <!-- gap = 145px -->
<text x="582" y="82" text-anchor="middle">Streamable HTTP</text>
```

### Rule 18: Center Rows of Equally-Spaced Boxes

When multiple boxes share a horizontal row, center the group within the viewBox - don't just start at a small x offset.

**Formula:** `start_x = (viewBox_width - total_row_width) / 2` where `total_row_width = N x box_width + (N-1) x gap`

```xml
<!-- BAD: 3 boxes starting at x=40 in an 800px viewBox - left-skewed -->
<rect x="40" ... width="150"/>
<rect x="220" ... width="150"/>
<rect x="400" ... width="180"/>

<!-- GOOD: 3 boxes centered (total width ~520px, start at (800-520)/2 = 140) -->
<rect x="120" ... width="160"/>
<rect x="310" ... width="160"/>
<rect x="500" ... width="160"/>
```

When a diagram has distinct row groups, add a visual separator between them:
```xml
<line x1="80" y1="290" x2="720" y2="290" stroke="#1e293b" stroke-dasharray="6 3"/>
<text x="400" y="307" fill="#64748b" font-size="8" text-anchor="middle">External Services</text>
```

### Rule 19: Bullet Markers for SVG Text Columns

For left-aligned list items in SVG (not centered via `text-anchor`), prefix each item with a bullet character `&#x2022;` to provide visual structure.

```xml
<!-- Without bullets - looks like floating text -->
<text x="160" y="320">Pydantic AI agents</text>
<text x="160" y="340">MCP tools (166+)</text>

<!-- With bullets - clearly a list -->
<text x="160" y="320">&#x2022; Pydantic AI agents</text>
<text x="160" y="340">&#x2022; MCP tools (166+)</text>
```

Keep all bullets at the same x position within a column. If using two columns with bullets, both columns should use the same bullet style.

---

### Common Shapes

```xml
<!-- Rounded rectangle (service box) -->
<rect x="100" y="50" width="160" height="60" rx="8" ry="8"
      fill="var(--diagram-primary, #0077BB)" stroke="none" />
<text x="180" y="85" text-anchor="middle" fill="var(--diagram-label, #FFFFFF)" font-size="14" font-weight="600">Service</text>

<!-- Database cylinder -->
<ellipse cx="180" cy="240" rx="50" ry="12" fill="var(--diagram-secondary, #009988)" />
<rect x="130" y="240" width="100" height="40" fill="var(--diagram-secondary, #009988)" />
<ellipse cx="180" cy="280" rx="50" ry="12" fill="var(--diagram-secondary, #009988)" />
<ellipse cx="180" cy="280" rx="50" ry="12" fill="var(--diagram-shadow, #000000)" fill-opacity="0.20" />
<text x="180" y="265" text-anchor="middle" fill="var(--diagram-label, #FFFFFF)" font-size="12">PostgreSQL</text>

<!-- Arrow connector -->
<line x1="180" y1="110" x2="180" y2="228" stroke="var(--diagram-arrow, #888)"
      stroke-width="2" marker-end="url(#arrowhead)" />

<!-- Dashed connector -->
<line x1="300" y1="80" x2="500" y2="80" stroke="var(--diagram-arrow, #888)"
      stroke-width="1.5" stroke-dasharray="6,4" marker-end="url(#arrowhead)" />
```

### Interactive Tooltips

Add `data-tooltip` attributes to SVG elements, then handle with vanilla JS:

```xml
<rect x="100" y="50" width="160" height="60" rx="8" data-tooltip="Handles user authentication and session management" />
```

```javascript
(function() {
  const tooltip = document.createElement('div');
  Object.assign(tooltip.style, {
    position: 'fixed', padding: '8px 12px', background: 'rgba(0,0,0,0.85)',
    color: '#fff', borderRadius: '6px', fontSize: '13px', maxWidth: '250px',
    pointerEvents: 'none', opacity: '0', transition: 'opacity 0.15s',
    zIndex: '1000', lineHeight: '1.4'
  });
  document.body.appendChild(tooltip);

  document.querySelectorAll('[data-tooltip]').forEach(el => {
    el.style.cursor = 'pointer';
    el.addEventListener('mouseenter', e => {
      tooltip.textContent = el.getAttribute('data-tooltip');
      tooltip.style.opacity = '1';
    });
    el.addEventListener('mousemove', e => {
      tooltip.style.left = (e.clientX + 12) + 'px';
      tooltip.style.top = (e.clientY - 30) + 'px';
    });
    el.addEventListener('mouseleave', () => {
      tooltip.style.opacity = '0';
    });
  });
})();
```

### CSS Custom Properties for Colors

Define in the presentation's `<style>` block so diagrams inherit the theme:

```css
:root {
  --diagram-primary: #0077BB;
  --diagram-secondary: #009988;
  --diagram-amber: #EE7733;
  --diagram-red: #CC3311;
  --diagram-purple: #3344AA;
  --diagram-arrow: #888;
  --diagram-bg: #2a2a2a;
  --diagram-text: #e0e0e0;
  --diagram-label: #FFFFFF;
  --diagram-shadow: #000000;
}

/* Light mode overrides */
@media (prefers-color-scheme: light) {
  :root {
    --diagram-arrow: #555;
    --diagram-bg: #ffffff;
    --diagram-text: #333;
  }
}
```

---

## Icons in Diagrams

Enhance diagrams with icons from the curated Lucide icon set. Icons use `stroke="currentColor"` so they inherit the surrounding color context.

### Setup: Include the Sprite

Add the hidden sprite block from `templates/icons/lucide-sprite.svg` at the top of the HTML `<body>`:

```html
<!-- Paste contents of templates/icons/lucide-sprite.svg here, wrapped in: -->
<svg xmlns="http://www.w3.org/2000/svg" style="display:none">
  <!-- symbol definitions from lucide-sprite.svg -->
</svg>
```

### Using Icons in Inline SVG Diagrams

Place `<use>` elements inside your SVG to reference icons from the sprite:

```xml
<!-- Inside a diagram SVG -->
<use href="#icon-database" x="155" y="62" width="20" height="20" style="color: var(--diagram-label, #FFFFFF);"/>
<use href="#icon-shield" x="415" y="62" width="20" height="20" style="color: var(--diagram-label, #FFFFFF);"/>
```

### Using Icons in HTML Slide Content

Use standalone inline `<svg>` elements with the `.icon` CSS class:

```html
<li>
  <svg class="icon" viewBox="0 0 24 24"><use href="#icon-database"/></svg>
  PostgreSQL for transactional data
</li>
```

### Icon CSS Helper

Include this in your presentation's `<style>` block:

```css
.icon {
  display: inline-block;
  vertical-align: middle;
  width: 1.2em;
  height: 1.2em;
  stroke: currentColor;
  fill: none;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
  flex-shrink: 0;
}
```

### Sizing Reference

| Context | Width/Height | Example |
|---------|-------------|---------|
| Inside large SVG box (160x80+) | 24x24 | Service icons in microservices diagram |
| Inside medium SVG box (140x55) | 20x20 | Stage icons in CI/CD pipeline |
| Inside small SVG box (110x40) | 16x16 | Pod icons in Kubernetes diagram |
| HTML inline with text | `.icon` class (1.2em) | Bullet list items |
| HTML card/heading | 2em or 32px | KPI dashboard card headers |

### Available Icons

See `references/icon-library.md` for the complete catalog with SVG path data. Key icons by domain:

| Domain | Recommended Icons |
|--------|-------------------|
| Infrastructure | `database`, `server`, `hard-drive`, `cpu`, `monitor` |
| Cloud/Network | `cloud`, `globe`, `wifi`, `network`, `router` |
| Security | `shield`, `shield-check`, `lock`, `key` |
| DevOps | `git-branch`, `git-commit-horizontal`, `terminal`, `package`, `container` |
| Code/API | `code`, `plug`, `webhook`, `settings` |
| Data/ML | `brain`, `activity`, `bar-chart-3`, `layers`, `workflow` |
| General | `users`, `building`, `box`, `folder`, `send`, `zap`, `credit-card` |
