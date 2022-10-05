import React from 'react'
import { A11y, Navigation, Pagination, Scrollbar } from 'swiper'
import { SwiperSlide, Swiper } from 'swiper/react'

const SlideCases = () => {
  return (
    
    <div className="slide">
      <div>
        <h1>Кейсы</h1>
        <h3>Текст о большой пользе рекламы и выгоде от ее использования, как она помогает предпринимателям его города и делает мир лучше.</h3>
        <div style={{width: '100%'}}>
        <Swiper
            //   allowTouchMove={false}
                autoplay={{
                    delay: 500,
                    disableOnInteraction: false
                }}
                loop={true}
              style={{width: 420, height: 400}}
              modules={[Pagination, Scrollbar, A11y]}
              spaceBetween={50}
              slidesPerView={1}
              pagination={{ clickable: true }}
              onSlideChange={() => console.log("slide change")}
              onSwiper={(swiper) => console.log(swiper)}
            >
            <SwiperSlide>
                <img style={{width: '100%', objectFit: 'scale-down'}} src='https://user-images.githubusercontent.com/10734493/33650878-bcd1c760-da9e-11e7-8427-07763d5d5e51.png'></img>
            </SwiperSlide>
            <SwiperSlide>
                <img style={{width: '100%', objectFit: 'scale-down'}} src='https://webrandum.net/mskz/wp-content/uploads/2020/02/image_1-8-1024x475.png'></img>
            </SwiperSlide>
            
        </Swiper>
        </div>
        <h3>
        
Тут карусель картинки наших кейсов (10 фото)Текст о полезности технологии, как она помогает развиваться бизнесам в городе партнера. Наши партнеры знакомятся с влиятельными людьми в своем городе а также становятся важными и нужными людьми в своем городе.
</h3>
      </div>
    </div>
  )
}

export default SlideCases