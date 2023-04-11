$(document).ready(function(){
    $('.header_burger').click(function(event){
        $('.header_burger,.header_menu').toggleClass('active');
    });
});

const button = document.querySelector('.footer_button')
console.log(button);
button.addEventListener('click', function setScrollIntoViewOptions(top){
    const news = document.querySelector('.line')
    news.scrollIntoView({
        block: "center",
        inline:"end",
        behavior:"smooth",
    })
});

const swiper = new Swiper('.swiper',{
    loop: true,
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
        dynamicBullets:true,
    },
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    }
});

const swipers = new Swiper('.swiperr',{
    loop: true,
    slidesPerView: 4,
    spaceBetween: 30,
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    }
});
const swiperss = new Swiper('.swiperrr',{
    loop: true,
    slidesPerView: 4,
    spaceBetween: 30,
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    }
});
