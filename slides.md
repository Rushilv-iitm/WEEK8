---
marp: true
title: ProductX Documentation Overview
description: Marp presentation for product documentation
theme: productx
paginate: true
paginate-align: center
footer: "ProductX Docs • 23f2000060@ds.study.iitm.ac.in"
math: katex
---

<style>
/* @theme productx */
section {
  background-color: #0f172a;
  color: #e5e7eb;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

section.lead h1 {
  font-size: 2.4em;
}

section.compact ul {
  font-size: 0.9em;
  line-height: 1.35;
}

h2 {
  color: #38bdf8;
}

code {
  font-size: 0.85em;
  background: #1e293b;
  padding: 4px;
  border-radius: 4px;
}

/* Page number styling */
section::after {
  font-size: 0.55em;
}
</style>

<!-- _class: lead -->

# ProductX Documentation Overview

Technical Writer – Platform Engineering  
**23f2000060@ds.study.iitm.ac.in**

---

## Documentation Goals

- Provide **version-controlled** documentation in Git
- Single source exportable to:
  - HTML presentations
  - PDF manuals
  - Printed guides
- Align docs with CI/CD to update on each release

---

<!-- _class: compact -->
<!-- _backgroundColor: #020617 -->

## Marp Workflow

- Author slides using **Markdown** (`slides.md`)
- Render via:
  - VS Code Marp extension
  - `@marp-team/marp-cli` in CI
- Export formats:
  - `HTML` for presentations
  - `PDF` for offline review
- Store with source code in repository

---

## Background Image Slide

![bg](images/architecture.png)

# High-Level Architecture

- API gateway
- Microservices for core features
- Background workers for async processing
- Observability: logs, metrics, traces

> Ensure `images/architecture.png` exists in the repo!

---

## Example Configuration Snippet

```yaml
# docs/config.yml
product:
  name: "ProductX"
  version: "1.4.0"
docs:
  source: "docs/"
  output: "dist/docs"
  formats:
    - html
    - pdf
