import React from "react";

const Slide1 = ({ data, links, slideData }) => {
  return (
    <div style={{backgroundImage: `url(${process.env.REACT_APP_API_URL + slideData?.image})`}} className="slide hero">
      <div>
        <h3>{slideData?.title}</h3>
        <h1>Презентация для Вас, {data?.user?.full_name}</h1>
        <h2>
          {slideData?.description}
        </h2>
        <ul className="hot_links">
          {links?.map(link => (
            <li><a href={`#page_${link?.order?.id}`}>{link?.name}</a></li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default Slide1;
