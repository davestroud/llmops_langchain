# Security Policy

## Supported Versions

We actively maintain the following versions of this repository:

| Version         | Supported          |
|-----------------|--------------------|
| Main Branch     | ✅ Yes             |
| Feature Branches| ⚠️ Limited Support |
| Deprecated Branches | ❌ No           |

Security updates are provided for the `main` branch and critical features. Ensure you use the latest version for full security compliance.

---

## Reporting a Vulnerability

If you discover a security vulnerability, please report it by following these steps:

1. **Contact Us:**  
   Send an email to [david@davidstroud.me](mailto:david@davidstroud.me) with a detailed description of the issue, including:
   - Steps to reproduce the issue
   - Potential impact of the vulnerability
   - Any suggested remediation steps

2. **Confidentiality:**  
   Please do not disclose the vulnerability publicly until we have addressed it. We aim to respond within **48 hours** of your report.

3. **Acknowledgment:**  
   Upon confirming the issue, we will acknowledge your report and work on fixing it. Security researchers may be credited for valid reports if they wish.

---

## Security Best Practices

To ensure secure usage of this repository, we recommend:
- **Regular Updates:** Always use the latest version from the `main` branch.
- **Environment Configuration:** Secure environment variables, API keys, and other sensitive data using tools like AWS Secrets Manager, HashiCorp Vault, or `.env` files with appropriate permissions.
- **Dependency Management:** Regularly update dependencies using tools like `pip`, `pipenv`, or `poetry` to mitigate risks associated with outdated packages.

---

## Known Issues

There are currently no known vulnerabilities. If any arise, they will be tracked in the repository’s [Issues](https://github.com/davestroud/llmops_langchain/issues) tab.

---

## Additional Information

For any additional questions, reach out to [david@davidstroud.me](mailto:david@davidstroud.me). You can also open a GitHub Discussion or Issue for general concerns.
