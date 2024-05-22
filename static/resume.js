const shortcuts = document.getElementsByClassName("resume-shortcut");
const level2Headers = document.querySelectorAll("h2");
for (const s of shortcuts) {
    s.addEventListener("click", function(e) {
        for (const h2 of level2Headers) {
            if (s.innerHTML == h2.innerHTML) {
                const rect = h2.getBoundingClientRect();
                window.scrollTo(rect.left + window.scrollX, rect.top + window.scrollY - 10);
                break;
            }
        }
    })
}