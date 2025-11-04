document.addEventListener('DOMContentLoaded', function() {
    const cross = document.querySelector('.crossemail-btn');
    const email = document.querySelector('.email-input');
    const crossmain = document.querySelector('.cross-btn');
    const search = document.querySelector('.search-input');
    const searchPlaceholder = document.querySelector('.search-placeholder');
    const chooseBtn = document.querySelector('.choose-btn');
    if (cross && email) {
        cross.addEventListener('click', function() {
            email.value = '';
            email.focus();
        });
    }
    if (crossmain && search) {
        crossmain.addEventListener('click', function() {
            search.value = '';
            search.focus();
            if (searchPlaceholder) {
                searchPlaceholder.style.display = 'block';
            }
        });
    }
    if (search && searchPlaceholder) {
        search.addEventListener('input', function() {
            if (this.value !== '') {
                searchPlaceholder.style.display = 'none';
            } else {
                searchPlaceholder.style.display = 'block';
            }
        });
    }
    if (chooseBtn) {
        const fileInput = document.createElement('input');
        fileInput.type = 'file';
        fileInput.accept = 'image/*';
        fileInput.style.display = 'none';
        fileInput.style.position = 'absolute';
        fileInput.style.left = '-9999px';
        document.body.appendChild(fileInput);
        chooseBtn.addEventListener('click', function() {
            fileInput.click();
        });
    }
});