(() => {
  "use strict";

  const copyButtons = [...document.querySelectorAll("[data-copy-target]")];
  const globalCopyStatus = document.getElementById("global-copy-status");

  function copyStatusFor(button) {
    return button.closest(".code-card")?.querySelector(".copy-status") ?? globalCopyStatus;
  }

  async function copyTarget(button) {
    const targetId = button.getAttribute("data-copy-target");
    const target = targetId ? document.getElementById(targetId) : null;
    if (!target) return;

    const text = target.textContent?.trim() ?? "";
    const status = copyStatusFor(button);
    const originalLabel = button.dataset.originalLabel ?? button.textContent ?? "Copy";
    button.dataset.originalLabel = originalLabel;

    try {
      if (!navigator.clipboard?.writeText) throw new Error("Clipboard API unavailable");
      await navigator.clipboard.writeText(text);
      button.textContent = "Copied";
      if (status) status.textContent = "Copied to clipboard.";
    } catch {
      const selection = window.getSelection();
      const range = document.createRange();
      range.selectNodeContents(target);
      selection?.removeAllRanges();
      selection?.addRange(range);
      button.textContent = "Selected";
      if (status) status.textContent = "Selected. Use your device copy command.";
    }

    window.setTimeout(() => {
      button.textContent = originalLabel;
      if (status) status.textContent = "";
    }, 2400);
  }

  for (const button of copyButtons) {
    button.addEventListener("click", () => copyTarget(button));
  }

  const header = document.querySelector("[data-site-header]");
  const menuButton = document.querySelector(".menu-button");
  const navigation = document.getElementById("primary-navigation");
  const desktopNavigation = window.matchMedia("(min-width: 721px)");

  function setMenu(open) {
    if (!header || !menuButton || !navigation) return;

    const isMobile = !desktopNavigation.matches;
    const isOpen = isMobile && open;
    header.dataset.menuOpen = String(isOpen);
    menuButton.setAttribute("aria-expanded", String(isOpen));
    navigation.inert = isMobile && !isOpen;
    navigation.setAttribute("aria-hidden", String(isMobile && !isOpen));
  }

  setMenu(false);

  menuButton?.addEventListener("click", () => {
    setMenu(menuButton.getAttribute("aria-expanded") !== "true");
  });

  navigation?.addEventListener("click", (event) => {
    const link = event.target instanceof Element ? event.target.closest("a") : null;
    if (link) setMenu(false);
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && menuButton?.getAttribute("aria-expanded") === "true") {
      setMenu(false);
      menuButton.focus();
    }
  });

  document.addEventListener("pointerdown", (event) => {
    if (!header || !(event.target instanceof Node) || header.contains(event.target)) return;
    setMenu(false);
  });

  desktopNavigation.addEventListener("change", () => setMenu(false));

  function updateHeaderState() {
    if (header) header.dataset.scrolled = String(window.scrollY > 12);
  }

  updateHeaderState();
  window.addEventListener("scroll", updateHeaderState, { passive: true });

  const sectionLinks = [...document.querySelectorAll('.site-nav a[href^="#"]')];
  const sections = sectionLinks
    .map((link) => {
      const id = link.getAttribute("href")?.slice(1);
      return id ? document.getElementById(id) : null;
    })
    .filter(Boolean);

  function setActiveSection(id) {
    for (const link of sectionLinks) {
      const active = link.getAttribute("href") === `#${id}`;
      if (active) link.setAttribute("aria-current", "location");
      else link.removeAttribute("aria-current");
    }
  }

  if ("IntersectionObserver" in window && sections.length > 0) {
    const observer = new IntersectionObserver(
      (entries) => {
        const visible = entries
          .filter((entry) => entry.isIntersecting)
          .sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];
        if (visible?.target.id) setActiveSection(visible.target.id);
      },
      { rootMargin: "-18% 0px -68% 0px", threshold: [0.05, 0.2, 0.5] },
    );

    for (const section of sections) observer.observe(section);
  }

  const year = document.getElementById("year");
  if (year) year.textContent = String(new Date().getFullYear());
})();
