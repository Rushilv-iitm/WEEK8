---
marp: true
theme: gaia
paginate: true
style: |
  section {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size: 30px;
  }
  h1 {
    color: #2980b9;
  }
---

# Product Documentation
## Technical Analysis & Algorithms

**Created by:** Technical Writing Team
**Email:** 23f2000060@ds.study.iitm.ac.in

---

## Performance Metrics

We define the system efficiency using standard mathematical notation.

The base lookup time for the documentation index is **constant time**, denoted inline as $\mathcal{O}(1)$.

However, the search ranking algorithm relies on the following summation:

$$
S(q, d) = \sum_{t \in q} tf(t, d) \cdot \log \left( \frac{N}{df(t)} \right)
$$

---

## Visual Architecture

![bg right:40%](https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800&q=80)

This slide uses **Marp Directives** to change the slide appearance:

1.  `_backgroundColor` sets the dark background.
2.  `_color` sets the text to light grey.
3.  `bg right` places the image on the right side.

---

# Thank You

Contact: 23f2000060@ds.study.iitm.ac.in
