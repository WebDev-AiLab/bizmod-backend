import { Icon } from "@iconify/react";
import { Map, Placemark, useYMaps } from "@pbe/react-yandex-maps";
import React, { useEffect, useRef, useState } from "react";

const SlideMap = ({data, slideData}) => {

  const [ready, setReady] = useState([])
  const ymaps = useYMaps(['Map', 'Placemark']);
    
  let placemarks = []

  const yandexMapRef = useRef(null)
  const mapRef = useRef(null);

  useEffect(() => {
    if (!ymaps || !mapRef.current) {
      return;
    }

    let myMap = new ymaps.Map(mapRef.current, {
      center: [55.76, 37.64],
      zoom: 10,
    });


    function setPlacemark(item, color) {
      myMap.geoObjects.add((new ymaps.Placemark([item?.geometry?.coordinates[1], item?.geometry?.coordinates[0]], {
        balloonContentHeader: item?.properties?.name,
        balloonContent: item?.properties?.name,
        balloonContentFooter: item?.properties?.name
      }, {
        preset: 'islands#redDotIcon',
        iconColor: color
      })))
    }

    
    data?.yandex_rest?.[0]?.features.forEach(item => {
      setPlacemark(item, '#d00')
    })

    
    data?.yandex_rest?.[1]?.features.forEach(item => {
      
      setPlacemark(item, '#0b0')
    })

    
    data?.yandex_rest?.[2]?.features.forEach(item => {
      
      setPlacemark(item, '#b0b')
    })

    
    data?.yandex_rest?.[3]?.features.forEach(item => {
      
      setPlacemark(item, '#f50')
    })

    
  
  // data?.yandex_rest?.[1]?.features.forEach(item => {
  //   placemarks.push({
  //     name: item?.properties?.name,
  //     color: '#d00',
  //     place: [item?.geometry?.coordinates[1], item?.geometry?.coordinates[0]]
  //   })
  // })
  
  // data?.yandex_rest?.[2]?.features.forEach(item => {
  //   placemarks.push({
  //     name: item?.properties?.name,
  //     color: '#b0b',
  //     place: [item?.geometry?.coordinates[1], item?.geometry?.coordinates[0]]
  //   })
  // })
  
  // data?.yandex_rest?.[3]?.features.forEach(item => {
  //   placemarks.push({
  //     name: item?.properties?.name,
  //     color: '#f50',
  //     place: [item?.geometry?.coordinates[1], item?.geometry?.coordinates[0]]
  //   })
  // })


    myMap.setBounds(myMap.geoObjects?.getBounds())

  }, [ymaps]);

  const handleMap = (api) => {


    // yandexMapRef.current?.setBounds(yandexMapRef.current?.geoObjects?.getBounds())
  }




  return (
    <div className="slide" id={`page_${slideData?.order?.id}`}>
      <h1>{data?.user?.full_name}, эти компании готовы с вами сотрудничать</h1>
      <div className="maps__wrapper">
        <div>
          <div>
            <h2>Кафе</h2>
            <div>
              {data?.yandex_rest?.[0]?.features?.map((item) => (
                <div className="maps_item">
                  <div className="maps_item__img green">
                    <Icon color="white" icon="fluent:food-pizza-20-filled" />
                  </div>
                  <div>
                    <h3>{item?.properties?.name}</h3>
                    <p>{item?.properties?.CompanyMetaData?.address}</p>
                    <a
                      target="_blank"
                      href={`https://yandex.ru/maps/org/${item?.properties?.CompanyMetaData?.id}`}
                    >
                      Перейти на Яндекс.Карты
                    </a>
                  </div>
                </div>
              ))}
            </div>
          </div>
          <div>
            <h2>Ресторан</h2>
            <div>
              {data?.yandex_rest?.[1]?.features?.map((item) => (
                <div className="maps_item">
                  <div className="maps_item__img red">
                    <Icon color="white" icon="ion:restaurant" />
                  </div>
                  <div>
                    <h3>{item?.properties?.name}</h3>
                    <p>{item?.properties?.CompanyMetaData?.address}</p>
                    <a
                      target="_blank"
                      href={`https://yandex.ru/maps/org/${item?.properties?.CompanyMetaData?.id}`}
                    >
                      Перейти на Яндекс.Карты
                    </a>
                  </div>
                </div>
              ))}
            </div>
          </div>
          <div>
            <h2>Торговый центр</h2>
            <div>
              {data?.yandex_rest?.[2]?.features?.map((item) => (
                <div className="maps_item">
                  <div className="maps_item__img purple">
                    <Icon color="white" icon="bxs:shopping-bag" />
                  </div>

                  <div>
                    <h3>{item?.properties?.name}</h3>
                    <p>{item?.properties?.CompanyMetaData?.address}</p>
                    <a
                      target="_blank"
                      href={`https://yandex.ru/maps/org/${item?.properties?.CompanyMetaData?.id}`}
                    >
                      Перейти на Яндекс.Карты
                    </a>
                  </div>
                </div>
              ))}
            </div>
          </div>
          <div>
            <h2>Магазин одежды</h2>
            <div>
              {data?.yandex_rest?.[3]?.features?.map((item) => (
                <div className="maps_item">
                  <div className="maps_item__img orange ">
                    <Icon color="white" icon="majesticons:t-shirt" />
                  </div>
                  <div>
                    <h3>{item?.properties?.name}</h3>
                    <p>{item?.properties?.CompanyMetaData?.address}</p>
                    <a
                      target="_blank"
                      href={`https://yandex.ru/maps/org/${item?.properties?.CompanyMetaData?.id}`}
                    >
                      Перейти на Яндекс.Карты
                    </a>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
        <div>
          <div ref={mapRef} className="yandex_map" />
          {/* <Map
            className="yandex_map"
            onLoad={handleMap}
            instanceRef={yandexMapRef}
            state={{
              center: [
                33,
                67,
              ],
              zoom: 8,
            }}
          > */}
            {/* {placemarks?.map((placemark) => (
              <Placemark
                options={{
                  iconColor: placemark.color,
                  iconContent: placemark?.name,
                }}
                defaultGeometry={placemark?.place}
              />
            ))} */}
          {/* </Map> */}
        </div>
      </div>
    </div>
  );
};

export default SlideMap;
