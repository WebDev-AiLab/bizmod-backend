import React, { useEffect, useState } from 'react'

const SlideCalculate = ({user}) => {

  const [population, setPopulation] = useState()

  useEffect(() => {
    fetchPopulation()
  }, [])

  
  const fetchPopulation = async () => {
    
    try {
      let res = await fetch(process.env.REACT_APP_API_URL + "/city/" + user?.city, {
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
      });
      let data = await res.json();


      setPopulation(data?.population);
      console.log(data);
    } catch (error) {
      console.log(error);
    }
  };


  return (
    
    <div className="slide">
      <div>
        <h1>{user?.full_name}, для вас расчет по г. {user?.city}</h1>
        <div className='calculate_info'>
            <div>
                <p>Размер г. {user?.city} составляет {user?.city_size}. Потенциальных клиентов в вашем городе {(population / 117)?.toFixed()}. Мы предоставим вам клиентскую базу, по которой вы будете работать. В среднем каждая четвертая организация становиться нашим клиентом и платит по 14000 рублей. Итого емкость рынка г. {user?.city} составляет {(population / 117 / 4 * 14000)?.toFixed()}.</p>
            </div>
            <div>
                <h3>Потенциальных клиентов в вашем городе</h3>
                <h1>{(population / 117)?.toFixed()}</h1>
                <h3>Организаций кому интересны услуги Wi-Fi маркетинга</h3>
                <h3>Емкость рынка нашей услуги</h3>
                <h1>{(population / 117 / 4 * 14 / 1000)?.toFixed()} млн.руб</h1>
                <h3>Организации готовы потратить на наши услуги</h3>
            </div>
        </div>
        <h3>Если хотите чтобы с вами связались нажмите на кнопку и мы перезвоним в самое ближайшее время</h3>
        <button>НАЖМИТЕ И МЫ ПРЕДОСТАВИМ КОНТАКТЫ РАБОТАЮЩИХ ПАРТНЕРОВ</button>
      </div>
    </div>
  )
}

export default SlideCalculate