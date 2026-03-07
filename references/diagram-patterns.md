# Diagram System Reference

Three-tier system for architectural and technical diagrams, ordered by token efficiency.

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
    { name: 'Auth Service', db: 'PostgreSQL', color: 'var(--diagram-blue)' },
    { name: 'Order Service', db: 'MongoDB', color: 'var(--diagram-green)' },
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
| Client-Server | client-server.svg | Architecture | 2 clients + 1 server | — | Simple request/response |
| Layered Architecture | layered-arch.svg | Architecture | 3 layers x 3 items | — | N-tier, clean arch |
| CI/CD Pipeline | cicd-pipeline.svg | DevOps | 5 stages | +1 | Build/deploy pipelines |
| Hub and Spoke | hub-and-spoke.svg | Platform | 6 spokes | +2 | Central platform |
| Cloud Three-Tier | cloud-three-tier.svg | Cloud | 4 zones | +1 app, +1 db | Cloud architecture |
| Kubernetes Cluster | kubernetes-cluster.svg | DevOps | 4 CP + 2x2 pods | +1 pod each | K8s deployments |
| Event Pub/Sub | event-driven-pubsub.svg | Backend | 3 pub + 3 sub | +1 each | Event-driven systems |
| ML Pipeline | ml-pipeline.svg | ML/AI | 3 stages | — | ML system design |
| C4 Context | c4-context.svg | Architecture | 1 person + 2 ext | +1 each | System context |
| Network Zones | network-zones.svg | Security | 3 zones x 2 svc | +1 each | Security architecture |
| API Gateway | api-gateway-auth.svg | Backend | 3 backend svc | — | API routing + auth |
| Pyramid/Roadmap | pyramid-roadmap.svg | General | 5 levels | — | Maturity stages |
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
      { name: 'User Service', db: 'PostgreSQL', color: 'var(--diagram-blue)' },
      { name: 'Order Service', db: 'DynamoDB', color: 'var(--diagram-green)' }
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
    const fill = rect.getAttribute('fill') || '#4A90D9';
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

## Tier 2: Mermaid.js

For diagrams that don't need pixel-level control. Mermaid renders from text syntax -- good for flowcharts, sequence diagrams, and ER diagrams.

### Setup

```html
<script src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"></script>
<script>
mermaid.initialize({
  startOnLoad: true,
  theme: 'dark',
  themeVariables: {
    primaryColor: '#4A90D9',
    primaryTextColor: '#e0e0e0',
    primaryBorderColor: '#6BA3D6',
    lineColor: '#888',
    secondaryColor: '#50C878',
    tertiaryColor: '#2a2a2a',
    fontFamily: 'system-ui, -apple-system, sans-serif',
    fontSize: '14px'
  }
});
</script>
```

### Container Pattern

```html
<div class="diagram-container" style="max-height:min(60vh,450px); overflow:hidden;">
  <pre class="mermaid">
    graph TD
    A[Client] --> B[API Gateway]
    B --> C[Service A]
    B --> D[Service B]
  </pre>
</div>
```

### 1. Flowchart

```
graph TD
    A[Start] --> B{Decision?}
    B -->|Yes| C[Process A]
    B -->|No| D[Process B]
    C --> E[End]
    D --> E

    style A fill:#4A90D9,stroke:#3a7bc8,color:#fff
    style E fill:#50C878,stroke:#3db066,color:#fff
```

Horizontal variant: use `graph LR` instead of `graph TD`.

### 2. Sequence Diagram

```
sequenceDiagram
    participant C as Client
    participant G as Gateway
    participant S as Service
    participant D as Database

    C->>G: HTTP Request
    G->>S: Forward + Auth
    S->>D: Query
    D-->>S: Results
    S-->>G: Response
    G-->>C: JSON Response

    Note over G,S: mTLS encrypted
```

### 3. Class Diagram

```
classDiagram
    class User {
        +String name
        +String email
        +login()
        +logout()
    }
    class Order {
        +int id
        +Date created
        +calculateTotal()
    }
    class Product {
        +String name
        +float price
    }
    User "1" --> "*" Order : places
    Order "*" --> "*" Product : contains
```

### 4. State Diagram

```
stateDiagram-v2
    [*] --> Idle
    Idle --> Processing : submit
    Processing --> Success : complete
    Processing --> Error : fail
    Error --> Processing : retry
    Success --> [*]
    Error --> [*] : cancel
```

### 5. Entity-Relationship Diagram

```
erDiagram
    USER ||--o{ ORDER : places
    ORDER ||--|{ LINE_ITEM : contains
    PRODUCT ||--o{ LINE_ITEM : "ordered in"
    USER {
        int id PK
        string name
        string email
    }
    ORDER {
        int id PK
        date created
        string status
    }
```

### Theme Variables for Light Mode

```javascript
mermaid.initialize({
  startOnLoad: true,
  theme: 'default',
  themeVariables: {
    primaryColor: '#4A90D9',
    primaryTextColor: '#333',
    primaryBorderColor: '#3a7bc8',
    lineColor: '#555',
    secondaryColor: '#50C878',
    tertiaryColor: '#f0f0f0'
  }
});
```

---

## Tier 3: Inline SVG (Fully Custom)

For diagrams that need precise positioning, custom shapes, or interactive elements.

### Responsive viewBox Pattern

```html
<svg viewBox="0 0 800 500" preserveAspectRatio="xMidYMid meet"
     style="width:100%; max-height:min(60vh,450px);" xmlns="http://www.w3.org/2000/svg">
  <!-- diagram content -->
</svg>
```

### Arrowhead Marker Definition

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

### Common Shapes

```xml
<!-- Rounded rectangle (service box) -->
<rect x="100" y="50" width="160" height="60" rx="8" ry="8"
      fill="var(--diagram-primary, #4A90D9)" stroke="none" />
<text x="180" y="85" text-anchor="middle" fill="#fff" font-size="14" font-weight="600">Service</text>

<!-- Database cylinder -->
<ellipse cx="180" cy="240" rx="50" ry="12" fill="var(--diagram-secondary, #50C878)" />
<rect x="130" y="240" width="100" height="40" fill="var(--diagram-secondary, #50C878)" />
<ellipse cx="180" cy="280" rx="50" ry="12" fill="var(--diagram-secondary-dark, #3db066)" />
<text x="180" y="265" text-anchor="middle" fill="#fff" font-size="12">PostgreSQL</text>

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
  --diagram-primary: #4A90D9;
  --diagram-secondary: #50C878;
  --diagram-amber: #F5A623;
  --diagram-red: #DC5A5A;
  --diagram-purple: #9B59B6;
  --diagram-arrow: #888;
  --diagram-bg: #2a2a2a;
  --diagram-text: #e0e0e0;
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
<use href="#icon-database" x="155" y="62" width="20" height="20" style="color: #fff;"/>
<use href="#icon-shield" x="415" y="62" width="20" height="20" style="color: #fff;"/>
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
