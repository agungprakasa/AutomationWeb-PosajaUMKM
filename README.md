# 🌐 Web Automation Framework — Selenium + Python

Automated web testing framework for enterprise web applications using **Selenium WebDriver** + **Python**, integrated with **Jenkins CI/CD** pipeline.

> Built and maintained by **Agung Prakasa** — Senior QA & DevSecOps Engineer  
> Production-tested on **Posaja UMKM**, **Posaja Mobile Web**, and **Pospay SuperApp** at PT. Pos Indonesia

---

## ✨ Key Features

- **Selenium WebDriver 4.x** — Latest web automation with relative locators & Chrome DevTools Protocol
- **Page Object Model (POM)** — Clean, maintainable, and scalable architecture
- **Jenkins CI/CD** — Automated pipeline triggered on every Git push
- **Cross-Browser** — Chrome, Firefox, Edge
- **Data-Driven Testing** — External test data via JSON / CSV / Excel
- **Auto Screenshot on Failure** — Captured report

---

## 📁 Project Structure

```
selenium-PosajaWeb/
├── tests/
│   ├── login.py              
│   ├── lupa_password.py           
│   └── toko.py
│   └── register.py             
├── Jenkinsfile                        # CI/CD pipeline definition
├── sonar-project.properties           # sonarqube
└── README.md
```

---

## ⚙️ Prerequisites

| Software      | Version  | Download |
|---------------|----------|----------|
| **Python**    | 3.9+     | [python.org](https://www.python.org/) |
| **Chrome**    | Latest   | [google.com/chrome](https://www.google.com/chrome/) |
| **ChromeDriver** | Match Chrome | [chromedriver.chromium.org](https://chromedriver.chromium.org/) |
| **Docker**    | 20.x+    | [docker.com](https://www.docker.com/) |
| **Allure CLI** | 2.x     | [docs.qameta.io](https://docs.qameta.io/allure/) |
| **Java JDK**  | 11+      | Required for Allure |

### Environment Variables

```bash
BASE_URL=https://your-app-url.com
TEST_USERNAME=your_test_user
TEST_PASSWORD=your_test_password
BROWSER=chrome          # chrome | firefox | edge
HEADLESS=false          # true for CI
SELENIUM_GRID_URL=http://localhost:4444/wd/hub   # optional
```

---

## 🚀 Getting Started

### 1. Clone

```bash
git clone https://github.com/agungprakasa/selenium-PosajaWeb.git
cd selenium-web-automation
```

### 2. Run Locally

```bash
# Run all tests
pyton3 tests/login.py
```

### 3. View Reports on Telegram

```bash
# Generate and open
#Token Telegram bot
```

---

## 🔧 Jenkins CI/CD Pipeline

The `Jenkinsfile just for Regression Test` :

```
Code Push → Install Deps → Run Tests (parallel) → SonarQube Scan
```

The `Jenkinsfile full` 

```
Code Push → Install Deps → Run Unit Tests → SonarQube Scan -> Depedency Check OWASP -> Build Docker -> Trivy Check -> Deploy Kubernetes/VM -> DAST(OWAST ZAP)
→ Regression Test
```

```

---

## 📊 Test Coverage -- Sample

| # | Feature        | File                   | TCs | Scenarios |
|---|----------------|------------------------|-----|-----------|
| 1 | Login          | `login.py`             | 3   | Valid/invalid login, remember me|
| 2 | Toko           | `toko.py`              | 1   | Toko  |
| 3 | Register       | `register.py`          | 1   | register  |
| 4 | Lupa Password  | `lupa_password.py`     | 1   | lupa password  |
|   | **Total**      |                        | **6** | |

---

## 🛠 Tech Stack

| Tool              | Purpose                         |
|-------------------|---------------------------------|
| **Selenium 4.x**  | Browser automation              |
| **Python 3.9+**   | Programming language            |
| **Jenkins**       | CI/CD pipeline                  |
| **SonarQube**     | Code quality analysis           |

---

## 📈 Results & Impact

> Applied in production at **PT. Pos Indonesia** across 3 major platforms

- ✅ **30% reduction** in manual regression testing time
- ✅ **20% fewer** post-release critical defects
- ✅ Integrated into GitLab CI — **runs on every push** to main branch
- ✅ **60+ automated test cases** covering Login, Payment, Logistics flows

---

## 👤 Author

**Agung Prakasa** — Senior QA & DevSecOps Engineer  
📧 agungprakasa49@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/agung-prakasa-769b53137/) · [Portfolio](https://agungprakasa.github.io/Myportfolio/) · [GitHub](https://github.com/agungprakasa)

---

*⭐ If this framework helps you, please give it a star!*
