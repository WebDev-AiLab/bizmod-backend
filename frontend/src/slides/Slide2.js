import React from "react";

const Slide2 = ({ user }) => {
  return (
    <div className="slide">
      <div>
        <h1>Это решение фин проблем и это лучше работы</h1>
        <h3>
        почему бизнес лучше работы, денег не хватает - это решение, ты будешь сам себе хозяин, разобраться не сложно. Это очень интересная сфера где получишь крутые навыки развития
        </h3>
        <ul>
          <li>Тезис 1</li>
          <li>Тезис 2</li>
          <li>Тезис 3</li>
        </ul>
        
        <video className='tech_video'></video>
        <h2>Cредний доход {user?.income}</h2>
      </div>
    </div>
  );
};

export default Slide2;
