import logo from "./logo.svg";
import "./App.css";
import { useParams, useSearchParams } from "react-router-dom";
import { useEffect, useState } from "react";
import "swiper/css";
import "swiper/css/navigation";
import "swiper/css/pagination";
import "swiper/css/scrollbar";
import { YMaps, Map, Placemark } from "@pbe/react-yandex-maps";
import Slide1 from "./slides/Slide1";
import SlideMap from "./slides/SlideMap";
import SlideCalculate from "./slides/SlideCalculate";
import Slide2 from "./slides/Slide2";
import Simple from "./slides/Simple";
import { Helmet } from "react-helmet";


// 3 +
// 4 +
// 5 +
// 6 +
// 8 +


function App() {
  const [data, setData] = useState({});
  const [pages, setPages] = useState({});
  const [error, setError] = useState({});
  const {email} = useParams();


  useEffect(() => {
    fetchData();
    fetchPages()
  }, []);


  const fetchData = async () => {
    
    try {
      let res = await fetch(process.env.REACT_APP_API_URL + "/view/" + email, {
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
      });
      let data = await res.json();
      setData(data);
      console.log(data);
    } catch (error) {
      setError(error);
      console.log(error);
    }
  };

  const fetchPages = async () => {
    
    try {
      let res = await fetch(process.env.REACT_APP_API_URL + "/constructor/pages", {
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
      });
      let data = await res.json();

      data.page = data.page.sort((a,b) => a?.order?.nomber - b?.order?.nomber)


      setPages(data);
      console.log(data);
    } catch (error) {
      setError(error);
      console.log(error);
    }
  };




  return (
    <YMaps>
      <Helmet>
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
      </Helmet>
      <div className="App">
        {error?.message ? (
          <div className="slide-container">
            <div className="slide">
              <h2>Ошибка загрузки</h2>
              <span>{error?.message}</span>
            </div>
          </div>
        ) : (
          <div className="slide-container">
            {/* <Swiper
              allowTouchMove={false}
              modules={[Navigation, Pagination, Scrollbar, A11y]}
              spaceBetween={50}
              slidesPerView={1}
              navigation
              pagination={{ clickable: true }}
              onSlideChange={() => console.log("slide change")}
              onSwiper={(swiper) => console.log(swiper)}
            > */}
            
            {/* <Slide1 user={data?.user}></Slide1> */}
            {pages?.page?.map(slideData => (
              // <SwiperSlide>
              <>
                {slideData.type_page?.name == 'Обычный' ? (
                  <>
                  {slideData?.fild ? (
                    <>
                    {slideData?.fild_value.includes(data?.user?.[slideData?.fild]) ? (
                      <Simple key={slideData?.id} user={data?.user} slideData={slideData} gallery={pages?.gallery}></Simple>
                    ) : null}
                    </>
                  ) : (
                    <Simple key={slideData?.id} user={data?.user} slideData={slideData} gallery={pages?.gallery}></Simple>
                    
                  )}
                  </>
                ) : slideData.type_page?.name == 'Карта' ? (
                  <SlideMap key={slideData?.id} slideData={slideData} data={data}/>
                ) : slideData.type_page?.name == 'Главный' ? (
                  <Slide1 key={slideData?.id} data={data} slideData={slideData} links={pages?.urls}/>
                ) : slideData.type_page?.name == 'Калькулятор' ? (
                  <SlideCalculate key={slideData?.id} user={data?.user} slideData={slideData} />
                ) : null}
              </>
              // </SwiperSlide>
            ))}
            {/* <SwiperSlide> */}
            {/* </SwiperSlide> */}
            {/* <SwiperSlide> */}
              {/* <Slide2 user={data?.user}></Slide2> */}
            {/* </SwiperSlide> */}
            {/* <SwiperSlide >
                  <SlideAbout user={data?.user}/>
            </SwiperSlide> */}
            {/* <SwiperSlide >
                  <SlideTech user={data?.user}/>
            </SwiperSlide> */}
            {/* <SwiperSlide >
                <SlideMap data={data}/>
            </SwiperSlide> */}
            {/* <SwiperSlide >
                <SlideSpheres data={data}/>
            </SwiperSlide> */}
            {/* <SwiperSlide >
                <SlideTestimotion data={data}/>
            </SwiperSlide> */}
            {/* <SwiperSlide >
                <SlideWhatToDo user={data?.user}/>
            </SwiperSlide> */}
            {/* <SwiperSlide >
                <SlideStatusTestimotion user={data?.user}/>
            </SwiperSlide> */}
            {/* <SwiperSlide >
                <SlideAboutDevice user={data?.user}/>
            </SwiperSlide> */}
            {/* <SwiperSlide >
                <SlideHPV user={data?.user}/>
            </SwiperSlide> */}
            {/* <SwiperSlide > */}
                {/* <SlideCalculate user={data?.user}/> */}
            {/* </SwiperSlide> */}
            {/* <SwiperSlide >
                <SlideAboutSupport user={data?.user}/>
            </SwiperSlide> */}
            {/* <SwiperSlide >
                <SlideCases user={data?.user}/>
            </SwiperSlide> */}
            {/* <SwiperSlide >
                <SlideVideoFeedbacks user={data?.user}/>
            </SwiperSlide> */}
            {/* <SwiperSlide >
                <SlideFeedbacks user={data?.user}/>
            </SwiperSlide> */}
            {/* <SwiperSlide > */}
                {/* <SlideAdvantages user={data?.user}/> */}
            {/* </SwiperSlide> */}
            {/* </Swiper> */}
          </div>
        )}
      </div>
    </YMaps>
  );
}

export default App;
