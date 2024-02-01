import React, { useContext, useState } from "react";
import { Context } from "../store/appContext";
import rigoImageUrl from "../../img/rigo-baby.jpg";
import "../../styles/home.css";

export const Home = () => {
  const { store, actions } = useContext(Context);
  const [inputData, setInputData] = useState({ name: "", price: 0 });

  const handleChange = (event) => {
    setInputData({ ...inputData, [event.target.name]: event.target.value });
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    actions.postItem(inputData);
  };

  return (
    <div>
      <h1>Agrega tus elementos...</h1>

      <form onSubmit={handleSubmit}>
        <input type="text" name="name" onChange={handleChange} />
        <input type="number" name="price" onChange={handleChange} />
        <button type="submit">agrega tu elemento</button>
      </form>

      <div>
        {store.items.map((item) => {
          return (
            <div key={item.id}>
              <div>{item.name}</div>
              <div>{item.price}</div>
            </div>
          );
        })}
      </div>
    </div>
  );
};
