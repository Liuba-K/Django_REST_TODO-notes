import React from 'react';

const Menu = () => {
    return (

        <nav class="navbar navbar-light bg-light">
          <div class="container-fluid">
            <p class="navbar-brand">Панель навигации</p>
            <form class="d-flex">
              <input class="form-control me-2" type="search" placeholder="Поиск" aria-label="Поиск"></input>
              <button class="btn btn-outline-success" type="submit">Поиск</button>
            </form>
          </div>
        </nav>


    )
};




export default Menu;

