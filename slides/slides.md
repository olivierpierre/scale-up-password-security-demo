---
title: "Password Security Demo"
author: "Pierre Olivier"
institute: "The University of Manchester, Department of Computer Science"
author: "Pierre Olivier"
email: "hello"
aspectratio: 1610
pdf-engine: xelatex
header-includes:
  - \input{header.tex}
  - \usepackage[most]{tcolorbox}
  - \setbeamercolor{background canvas}{bg=white}
  - \newcommand{\insertemail}{\href{mailto:pierre.olivier@manchester.ac.uk}{pierre.olivier@manchester.ac.uk}}

---
# Objective

- **Password hygiene/good practices** include among other things:
  - Passwords should be **long**, i.e., made of numerous characters/words **AND**
  - Passwords should be **complex**, i.e., made of various types of characters


Why such rules?

\pause

\vfill
\begin{alertblock}{Ethical Use Disclaimer}

\begin{itemize}
\item This demo introduces techniques that are commonly associated with offensive security, their purpose in this context is purely educational
\item You are expected to use the knowledge and skills from this demo responsibly and ethically
\item Any use of these techniques outside of authorised, educational, or professional penetration testing contexts is strictly prohibited and may be illegal
\end{itemize}

\end{alertblock}

---

# Data Breaches

- Data breaches are very common
- One of the worst type of personal data that can be stolen are **passwords**

::: columns
:::: {.column width=60%}

\begin{tcolorbox}[
  colback=white,
  colframe=black!30,
  boxrule=0.5pt,
  arc=2mm,
  borderline={0.5pt}{0pt}{black!25},
]
\includegraphics[width=\linewidth]{include/guardian-breach.png}
\end{tcolorbox}

::::

:::: {.column width=40%}
\begin{tcolorbox}[
  colback=white,
  colframe=black!30,
  boxrule=0.5pt,
  arc=2mm,
  borderline={0.5pt}{0pt}{black!25},
]
\includegraphics[width=\linewidth]{include/trakt-breach}
\end{tcolorbox}
::::

:::

# What's an Encrypted Password?

\center
\includegraphics[width=.9\linewidth]{include/hash.pdf}


- Plain text passwords are transformed into **hashed (encrypted) passwords** stored into web services databases
  - Goal is to avoid storing plain text passwords

\pause

- Authentication process:
  1. Prompt user for plain text password attempt
  2. Hash the attempt
  3. Compare to the hash of the correct password in the database: if they match, authentication succeeds

# Cracking Passwords

::: columns

:::: {.column width=40%}
\center
\includegraphics[width=.77\linewidth]{include/crack.pdf}
::::

:::: {.column width=60%}
- Hackers commonly steal lists of **hashed passwords** from online services and applications
- Their next goal is then to **revert the hashes into plain text passwords**

::::

:::

# Cracking Passwords (2)

::: columns

:::: {.column width=40%}
\center
\includegraphics[width=.77\linewidth]{include/crack.pdf}
::::

:::: {.column width=60%}
- Directly reverting a hash back into the corresponding password is impossible
  - Hash functions are unidirectional transformations

\pause

- Common approach: attacker hashes themselves possible passwords and compare to stolen hashes
  - If they match: password recovered

\pause

1. **Brute force attack:** try every possible combination of characters
2. **Dictionary attack:** try commonly used passwords, e.g., dictionary words

\pause

\vspace{0.5cm}
- Very efficient on weak passwords with the processing power of modern computers
::::

:::

#

\center
<div style="text-align:center; font-size:2em;">
Demo 1: Cracking a Simple Password
</div>

# MD5 Cracking Speed

\center
\includegraphics[width=.77\linewidth]{include/benchmark.pdf}

#

\center
<div style="text-align:center; font-size:2em;">
Demo 2: Cracking a List of Hashes
</div>

# Password Hygiene

Good practices for strong password security **make it very hard/impossible to revert hashes**

::: columns

:::: column

- On the end user side:
  - **Choose long (12+ characters) passwords**
  - Choose passwords with a wide set of characters: digits, special characters, etc.
::::

:::: column
- On the application/website developer side:
  - Force user to choose long/varied passwords
  - Use strong hash methods, make it at least a bit computationally expensive to hash
  - Combine passwords with random data (salt) before hashing
::::

:::

# Slides + Demo are Online

- You can try this demo (responsibly!) at home
- Instructions on how to reproduce it + PDF of the slides are available online:

\center
\includegraphics[width=.45\linewidth]{include/github-qr-code.pdf}
\href{https://github.com/olivierpierre/scale-up-password-security-demo}{\texttt{https://github.com/olivierpierre/scale-up-password-security-demo}}
