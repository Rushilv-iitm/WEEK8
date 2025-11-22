---
marp: true
theme: gaia
paginate: true
author: "Technical Writer"
description: "Product Documentation for OptiSearch Algorithm"
backgroundColor: #fff
---

<style>
:root {
  --color-highlight: #d63031;
  --color-brand: #0984e3;
}

section {
  font-family: 'Segoe UI', Helvetica, sans-serif;
  font-size: 28px;
  color: #2d3436;
}

h1, h2 {
  color: var(--color-brand);
}

code {
  background: #dfe6e9;
  color: #d63031;
}

/* Footer styling */
footer {
  font-size: 12px;
  color: #636e72;
}
</style>

# OptiSearch Engine v2.0
## Technical Documentation & Performance Metrics

**Contact:** 23f2000060@ds.study.iitm.ac.in
*Department of Data Science*

---

# Overview

OptiSearch is a lightweight, JSON-based search indexer designed for static documentation sites.

**Key Features:**
* Zero-dependency architecture
* Client-side fuzzy search
* <span style="color: var(--color-highlight);">**Markdown support**</span> out of the box

---

![bg cover brightness:0.4](https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1920)

# System Architecture

The architecture relies on a distributed node system.

> "Scalability is not an afterthought, it is the foundation."

*Background: Abstract Network Topology*

---

# Algorithmic Complexity

We utilize a modified Merge Sort implementation for indexing.

**Time Complexity Calculation:**
The recurrence relation for the indexing speed is defined as:

$$
T(n) = 2T\left(\frac{n}{2}\right) + O(n)
$$

Solving this recurrence yields a complexity of:

$$
\Theta(n \log n)
$$

Where $n$ is the number of documents in the corpus.

---

# Implementation Details

<div class="columns">

<div>

### Installation
To install the engine, run the following in your CI/CD pipeline:

```bash
npm install optisearch-core
