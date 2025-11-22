---
marp: true
title: Product Documentation Presentation
author: Rushil V
theme: custom-product
paginate: true
footer: "📧 23f2000060@ds.study.iitm.ac.in"
---

<!-- _class: lead -->

# 🧩 Product Documentation  
## using **Marp + Version Control**

---

<!-- _backgroundColor: #1a1a1a -->
<!-- _color: #ffffff -->

### Why Markdown Documentation?

- Developer-friendly  
- Version-controlled (Git)
- Reusable as:
  - PDF
  - Slides
  - Docs  
- No vendor lock-in

> "_Write once, use everywhere_"

---

## 📦 Documentation Goals

| Feature | Requirement |
|--------|-------------|
| Maintainable | Git-based |
| Multi-format | HTML, PDF, PPTX |
| Automated | CI/CD Builds |
| Customizable | Theming & assets |

---

<!-- _header: **Algorithm Complexity** -->

### 💡 Complexity Example (Search Module)

Inline math:  
`Average Lookup → $O(\log n)$`

Block math:

$$
T(n) = T(n/2) + O(1) \Rightarrow O(\log n)
$$

---

<!-- _class: lead -->
<!-- _footer: "*Confidential — Internal Use Only*" -->

# 🗂️ Folder Structure (Recommended)

docs/
├── slides.md # Presentation (this file)
├── images/ # Assets
├── themes/ # Custom CSS theme
└── package.json # Build scripts

yaml
Copy code

---

<!-- _backgroundImage: url(images/background-product.jpg) -->
<!-- _backgroundSize: cover -->

# 📸 Product Overview

*(Slide with background image)*  

---

### 🔧 Build Automation (package.json)

```json
{
  "scripts": {
    "start": "marp -s .",
    "build": "marp slides.md -o dist/slides.html",
    "pdf": "marp slides.md --pdf --allow-local-files",
    "pptx": "marp slides.md --pptx"
  }
}
🎨 Custom Theme Definition
(themes/custom-product.css)

css
Copy code
/* Custom Marp Theme */
section {
  font-family: "Segoe UI", sans-serif;
  background: #fefefe;
  color: #222;
}
h1, h2 { color: #004aad; }
footer { font-size: 0.7rem; color: #555; }
📩 Contact
Technical Writer: Rushil V
Email: 23f2000060@ds.study.iitm.ac.in
GitHub URL (Raw File):
https://raw.githubusercontent.com/Rushilv-iitm/WEEK8/refs/heads/main/slides.md

yaml
Copy code

---

### 💡 Next Step  
Create this folder in your repo:

WEEK8/
├── slides.md (paste the above content)
├── images/
│ └── background-product.jpg
└── themes/
└── custom-product.css

vbnet
Copy code

Would you like me to:

📌 **Generate the background image automatically?**  
🎨 **Make a more advanced custom theme?**  
🔧 **Add CI/CD build using GitHub Actions?**

Just tell me! 😊
