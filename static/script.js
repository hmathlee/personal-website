const navbar = document.getElementsByClassName("navbar")[0];
for (const li of navbar.children) {
    const anchor = li.children[0];
    if (anchor.href == window.location.href) {
        anchor.style.backgroundColor = "white";
        anchor.style.color = "black";
        break;
    }
}