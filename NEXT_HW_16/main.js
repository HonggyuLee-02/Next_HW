function clickNav() {
    var banner = document.querySelector('.banner h1');
    var description = document.querySelector('.banner div');

    var dict = {
        About: 'Custom Software Development Company',
        Products: 'View Our Newest Products!',
        Technology: 'This is our newest Technology.',
        Downloads: 'Download our CV here.',
    };

    var buttonText = document.activeElement.getAttribute('data-button');
    banner.textContent = buttonText;
    description.textContent = dict[buttonText];
}

var acc = document.querySelectorAll('.buttons button');
for (var i = 0; i < 4; i++) {
    acc[i].addEventListener('click', clickNav);
}
