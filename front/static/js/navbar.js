function menuShow() {
    let mobileMenu = document.querySelector('.mobile-menu');
    let icon = document.querySelector('.icon');
    
    // Verifica se o ícone e o menu existem antes de manipular
    if (!mobileMenu || !icon) return;

    // Alterna a classe 'open' para mostrar ou esconder o menu
    if (mobileMenu.classList.contains('open')) {
        mobileMenu.classList.remove('open');
        icon.src = "../imgs/MenuDefinitivo.svg";  // Muda para o ícone de menu
    } else {
        mobileMenu.classList.add('open');
        icon.src = "../imgs/X.svg";  // Muda para o ícone de "fechar"
    }
}
