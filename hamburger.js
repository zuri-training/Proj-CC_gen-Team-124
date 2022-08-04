const hamburgerButton = document.getElementById('hamburger-btn');

const toggleHamburgerMenu = () => {
    const hamburgerMenu = document.getElementById('hamburger-menu');
    
    hamburgerMenu.classList.toggle('hide');
}

hamburgerButton.addEventListener('click', toggleHamburgerMenu);