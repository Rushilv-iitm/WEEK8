---
marp: true
theme: custom-docs
paginate: true
header: 'Product Documentation | v2.0'
footer: '23f2000060@ds.study.iitm.ac.in'
style: |
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Fira+Code&display=swap');
  
  section {
    background-color: #ffffff;
    font-family: 'Inter', sans-serif;
    color: #1a1a1a;
    padding: 60px 80px;
  }
  
  h1 {
    color: #0066cc;
    font-weight: 700;
    font-size: 2.5em;
    margin-bottom: 0.5em;
    border-bottom: 4px solid #0066cc;
    padding-bottom: 0.3em;
  }
  
  h2 {
    color: #0052a3;
    font-weight: 600;
    font-size: 1.8em;
    margin-top: 1em;
  }
  
  h3 {
    color: #333333;
    font-weight: 600;
    font-size: 1.3em;
  }
  
  code {
    background-color: #f5f5f5;
    padding: 2px 6px;
    border-radius: 4px;
    font-family: 'Fira Code', monospace;
    color: #d73a49;
  }
  
  pre {
    background-color: #2d2d2d;
    padding: 20px;
    border-radius: 8px;
    border-left: 4px solid #0066cc;
  }
  
  pre code {
    background-color: transparent;
    color: #f8f8f2;
  }
  
  blockquote {
    border-left: 4px solid #0066cc;
    padding-left: 20px;
    margin: 20px 0;
    font-style: italic;
    background-color: #f0f7ff;
    padding: 15px 20px;
    border-radius: 4px;
  }
  
  table {
    border-collapse: collapse;
    width: 100%;
    margin: 20px 0;
  }
  
  th {
    background-color: #0066cc;
    color: white;
    padding: 12px;
    text-align: left;
  }
  
  td {
    padding: 10px 12px;
    border-bottom: 1px solid #e0e0e0;
  }
  
  tr:hover {
    background-color: #f5f5f5;
  }
  
  ul, ol {
    line-height: 1.8;
  }
  
  strong {
    color: #0066cc;
    font-weight: 600;
  }
  
  header {
    font-size: 0.8em;
    color: #666;
  }
  
  footer {
    font-size: 0.7em;
    color: #999;
  }
  
  section.title {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
  }
  
  section.title h1 {
    color: white;
    border-bottom: none;
    font-size: 3.5em;
    margin-bottom: 0.3em;
  }
  
  section.title p {
    font-size: 1.3em;
    margin: 10px 0;
  }
  
  .columns {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 40px;
  }
  
  .box {
    background-color: #f0f7ff;
    padding: 20px;
    border-radius: 8px;
    border-left: 4px solid #0066cc;
  }
---

<!-- _class: title -->
<!-- _paginate: false -->
<!-- _header: "" -->
<!-- _footer: "" -->

# API Gateway Documentation

**Enterprise-Grade API Management Platform**

Version 2.0 | 2024

---

# Table of Contents

1. **Introduction** - Overview and Architecture
2. **Getting Started** - Setup and Configuration
3. **Core Features** - API Management Capabilities
4. **Performance Metrics** - Benchmarks and Optimization
5. **Security** - Authentication and Authorization
6. **Best Practices** - Implementation Guidelines

---

# Introduction

## What is API Gateway?

API Gateway is a high-performance, scalable API management solution designed for modern microservices architectures.

**Key Benefits:**

- **High Throughput**: Handle millions of requests per second
- **Low Latency**: Sub-millisecond response times
- **Flexible Routing**: Dynamic path-based and header-based routing
- **Built-in Security**: OAuth2, JWT, API Keys, and more

---

# Architecture Overview

<div class="columns">

<div>

## Components

- **Gateway Core**: Request processing engine
- **Rate Limiter**: Token bucket algorithm
- **Load Balancer**: Round-robin and least-connection
- **Cache Layer**: Redis-backed response cache

</div>

<div class="box">

### Performance Profile

Time Complexity: $O(1)$ for routing
Space Complexity: $O(n)$ for cache

**Throughput Equation:**

$
T = \frac{R \times C}{L + P}
$

Where: $T$ = Throughput, $R$ = Request rate, $C$ = Connections, $L$ = Latency, $P$ = Processing time

**Little's Law:**

$
L = \lambda \times W
$

$L$ = avg requests in system, $\lambda$ = arrival rate, $W$ = avg time in system

</div>

</div>

---

<!-- _backgroundColor: #f0f7ff -->

# Quick Start Guide

## Installation

```bash
# Install via npm
npm install @company/api-gateway

# Or using Docker
docker pull company/api-gateway:latest
docker run -p 8080:8080 company/api-gateway:latest
```

## Basic Configuration

```yaml
gateway:
  port: 8080
  routes:
    - path: /api/v1/*
      backend: https://backend.example.com
      methods: [GET, POST, PUT, DELETE]
```

---

# Core Features

## 1. Request Routing

Route requests based on:
- URL paths and patterns
- HTTP methods and headers
- Query parameters
- Custom rules

## 2. Rate Limiting

Implement the **Token Bucket Algorithm**:

$
\text{tokens}(t) = \min\left(b, \text{tokens}(t-1) + r \times \Delta t\right)
$

Where $b$ = bucket capacity, $r$ = refill rate, $\Delta t$ = time elapsed

**Request acceptance condition:**

$
\text{accept} = 
\begin{cases} 
\text{true} & \text{if tokens}(t) \geq c \\
\text{false} & \text{otherwise}
\end{cases}
$

where $c$ is the cost per request (usually 1)

---

# Capacity Planning Mathematics

## Throughput Calculation

**Maximum Theoretical Throughput:**

$
T_{\max} = \frac{C \cdot N}{L_{\text{avg}} + P_{\text{avg}}}
$

$C$ = connections per server, $N$ = number of servers, $L_{\text{avg}}$ = avg latency, $P_{\text{avg}}$ = avg processing time

## Percentile Calculations

For sorted response times $[t_1, t_2, \ldots, t_n]$:

$
P_{xx} = t_{\left\lceil \frac{xx \cdot n}{100} \right\rceil}
$

**Tail Latency Amplification** (when calling $k$ services):

$
P_{99}^{\text{composite}} = 1 - (1 - P_{99}^{\text{single}})^k
$

---

# Performance Benchmarks

| Metric | Value | Target |
|--------|-------|--------|
| Throughput | 50K req/s | 40K req/s |
| P50 Latency | 2ms | < 5ms |
| P99 Latency | 15ms | < 20ms |
| CPU Usage | 45% | < 60% |
| Memory Usage | 2.1 GB | < 3 GB |

> **Note**: Benchmarks performed on AWS c5.2xlarge instances with 8 vCPUs and 16GB RAM

---

# Security Features

## Authentication Methods

1. **API Keys** - Simple token-based auth
2. **OAuth 2.0** - Industry standard authorization
3. **JWT Tokens** - Stateless authentication
4. **mTLS** - Certificate-based mutual authentication

## Security Headers

```javascript
headers: {
  'X-Frame-Options': 'DENY',
  'X-Content-Type-Options': 'nosniff',
  'Strict-Transport-Security': 'max-age=31536000',
  'Content-Security-Policy': "default-src 'self'"
}
```

---

<!-- _backgroundImage: url('https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1200&q=80') -->
<!-- _color: white -->
<!-- _header: "" -->

<div style="background-color: rgba(0,0,0,0.7); padding: 40px; border-radius: 12px;">

# Global Scale

## Deployed Across 12 Regions

- **North America**: 4 zones
- **Europe**: 4 zones
- **Asia Pacific**: 3 zones
- **South America**: 1 zone

**99.99% Uptime SLA**

</div>

---

# Mathematical Foundations

## Queueing Theory

**M/M/1 Queue Response Time:**

$
W = \frac{1}{\mu - \lambda}
$

where $\mu$ = service rate, $\lambda$ = arrival rate (requires $\lambda < \mu$)

**System Utilization:**

$
\rho = \frac{\lambda}{\mu}, \quad 0 \leq \rho < 1
$

**Average Queue Length (Little's Law):**

$
L = \lambda W = \frac{\rho}{1-\rho}
$

---

# Advanced Configuration

## Load Balancing Strategies

```typescript
interface LoadBalancerConfig {
  strategy: 'round-robin' | 'least-connection' | 'ip-hash';
  healthCheck: {
    interval: number;
    timeout: number;
    unhealthyThreshold: number;
  };
  backends: Backend[];
}
```

**Algorithm Complexity:**
- Round Robin: $O(1)$ per request
- Least Connection: $O(n)$ per request, can be optimized to $O(\log n)$ with heap
- IP Hash: $O(1)$ with consistent hashing

**Consistent Hashing Load Balance:**

$
\sigma = \sqrt{\frac{1}{m} \sum_{i=1}^{m} \left(\frac{n_i}{n} - \frac{1}{m}\right)^2}
$

where $\sigma$ is standard deviation, $m$ = servers, $n_i$ = load on server $i$, $n$ = total load

---

# Monitoring & Observability

<div class="columns">

<div>

## Metrics Collection

- Request count and rate
- Response time percentiles
- Error rates by endpoint
- Backend health status

</div>

<div>

## Integration Points

- **Prometheus** - Metrics scraping
- **Grafana** - Visualization
- **Jaeger** - Distributed tracing
- **ELK Stack** - Log aggregation

</div>

</div>

```promql
# Example PromQL query
rate(api_requests_total[5m])
```

---

# Best Practices

## 1. Circuit Breaking

Prevent cascade failures with circuit breaker pattern:

- **Closed**: Normal operation
- **Open**: Fast-fail on errors (threshold exceeded)
- **Half-Open**: Test recovery with limited requests

## 2. Caching Strategy

```javascript
cache: {
  ttl: 300,              // 5 minutes
  maxSize: 1000,         // Max cached items
  strategy: 'LRU'        // Least Recently Used
}
```

---

# Troubleshooting Guide

| Issue | Possible Cause | Solution |
|-------|---------------|----------|
| High latency | Backend slow | Enable caching, check backend |
| 503 errors | Rate limiting | Increase rate limits |
| Memory leak | Cache overflow | Set maxSize limits |
| Connection timeout | Network issues | Adjust timeout settings |

> **Pro Tip**: Enable debug logging with `LOG_LEVEL=debug` for detailed diagnostics

---

# API Reference

## Gateway Configuration

```typescript
interface GatewayConfig {
  port: number;
  host: string;
  cors: CORSConfig;
  rateLimit: RateLimitConfig;
  routes: Route[];
  middleware: Middleware[];
}
```

**Documentation**: https://docs.company.com/api-gateway

**Contact**: 23f2000060@ds.study.iitm.ac.in

---

# Performance Optimization

## Key Optimization Techniques

1. **Connection Pooling**: Reuse TCP connections
   - Optimal pool size: $n = \left\lceil \frac{R_{\max}}{C_b} \right\rceil$ where $R_{\max}$ = max concurrent requests, $C_b$ = connections per backend

2. **Request Batching**: Combine multiple requests
   - Amortized complexity: $O(n) \rightarrow O(1)$ for $n$ requests
   - Latency reduction: $L_{\text{batched}} = \frac{L_{\text{single}}}{b}$ where $b$ = batch size

3. **Compression**: Reduce payload size
   - Compression ratio: $r = \frac{S_{\text{original}}}{S_{\text{compressed}}}$
   - gzip: $r \approx 3-10$ for JSON/text
   - Transfer time saved: $\Delta T = \frac{S_{\text{original}} - S_{\text{compressed}}}{B}$ where $B$ = bandwidth

---

# Deployment Strategies

<div class="box">

## Blue-Green Deployment

1. Deploy new version to "green" environment
2. Run smoke tests and validation
3. Switch traffic from "blue" to "green"
4. Keep "blue" as rollback option

**Rollback Time**: < 30 seconds

</div>

## Canary Releases

Gradually roll out to percentage of traffic:
- 5% → 25% → 50% → 100%
- Monitor error rates at each stage
- Auto-rollback on threshold breach

---

# Upcoming Features

## Roadmap Q1 2025

- [ ] **GraphQL Support** - Native GraphQL gateway
- [ ] **gRPC Protocol** - HTTP/2 and gRPC support
- [ ] **AI-Powered Analytics** - ML-based anomaly detection
- [ ] **Multi-Cloud Mesh** - Seamless cloud provider integration

**Algorithm Enhancement**: Implementing consistent hashing with bounded loads for better load distribution

**Bounded Load Formula:**

$
\text{load}(s) \leq \left\lceil \frac{1 + \epsilon}{n} \cdot L_{\text{total}} \right\rceil
$

where $\epsilon$ = load imbalance factor, $n$ = servers, $L_{\text{total}}$ = total load

**Jump Consistent Hash:**

$
h(k, b) = \arg\max_{j \in [0,b)} \left\{ j : \text{random}(k, j) < \frac{j}{b} \right\}
$

Provides $O(1)$ average case and $O(\log n)$ worst case for bucket assignment

---

<!-- _class: title -->
<!-- _paginate: false -->

# Thank You

## Questions?

**Documentation**: https://docs.company.com
**Support**: support@company.com
**Email**: 23f2000060@ds.study.iitm.ac.in

**GitHub**: https://github.com/company/api-gateway
**Slack**: #api-gateway-support

---

# Appendix: References

1. **RFC 7231** - HTTP/1.1 Semantics and Content
2. **RFC 6749** - OAuth 2.0 Authorization Framework
3. **RFC 7519** - JSON Web Token (JWT)
4. **Karger et al.** - Consistent Hashing and Random Trees
5. **Fowler, M.** - Patterns of Enterprise Application Architecture

**Version Control**: This presentation is maintained at:
```
https://raw.githubusercontent.com/company/docs/main/api-gateway-v2.md
```

---

<!-- _paginate: false -->
<!-- _footer: "" -->

# Speaker Notes

**For Slide 1 (Title)**: Welcome everyone. Today we'll cover our API Gateway platform, focusing on architecture, performance, and best practices.

**For Slide 5 (Architecture)**: Note the mathematical complexity - O(1) routing is achieved through hash-based lookups. The throughput equation helps calculate system capacity.

**For Slide 7 (Performance)**: These benchmarks are from production. P99 latency is critical for user experience.

**For Slide 11 (Optimization)**: Connection pooling reduces overhead significantly. The formula helps calculate optimal pool size.
