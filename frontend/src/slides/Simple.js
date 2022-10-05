import React, { useEffect, useState } from 'react'
import { A11y, Navigation, Pagination, Scrollbar } from 'swiper'
import { SwiperSlide, Swiper } from 'swiper/react'
import template from '../utils/template'

const Simple = ({user, slideData, gallery}) => {

  const [images, setImages] = useState([])

  useEffect(() => {
    let imgs = gallery.filter(galleryItem => galleryItem?.page == slideData?.id)
    setImages(imgs)
  }, [])


  let sub_description = slideData?.sub_description


  sub_description = template(sub_description, user)



  return (
    
    <div className="slide" id={`page_${slideData?.order?.id}`}>
        <h1>{slideData?.title}</h1>
        <h3>{slideData?.sub_title}</h3>
        <div style={{width: '100%'}}>
        {images?.length > 0 &&  (
          <Swiper
              allowTouchMove={true}
                autoplay={{
                    delay: 500,
                    disableOnInteraction: false
                }}
                loop={true}
              style={{width: '100%', maxWidth: 800, height: 420 }}
              modules={[Pagination, Scrollbar, A11y]}
              spaceBetween={50}
              slidesPerView={1}
              pagination={{ clickable: true }}
              onSlideChange={() => console.log("slide change")}
              onSwiper={(swiper) => console.log(swiper)}
            >
              {images?.map( image =>(
                <SwiperSlide>
                <img style={{width: '100%', objectFit: 'scale-down', height: '420px'}} src={process.env.REACT_APP_API_URL + image?.image}></img>
                </SwiperSlide>
              ))}
            
        </Swiper>
        )}
        {slideData?.video_url && (
          <video controls src={slideData?.video_url} className='tech_video'></video>
        )}
        {slideData?.image && (
          <img src={process.env.REACT_APP_API_URL + slideData?.image}></img>
        )}
        </div>
        <h2>
        {slideData?.description}
        </h2>
        <p>
        {sub_description}
        </p>
        <h3>
        {slideData?.pre_button_text}
        </h3>
        {slideData?.button_text && (
          <a href={slideData?.button_link}><button>{slideData?.button_text}</button></a>
        )}
    </div>
  )
}

export default Simple