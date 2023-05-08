import React from "react";
import './menu.css';
import {NavLink} from 'react-router-dom';

function Menu() {

	return(
		<div className="menu">
			<NavLink to={'/'}><img src="img/menu/logo.svg" alt="OH"  id="logo"/></NavLink>
			<ul className="naw">
				<li><NavLink to={'#'}><img src="img/menu/repair.svg" alt="repair" />Ремонт</NavLink></li>
				<li><NavLink to={'#'}><img src="img/menu/performers.svg" alt="performers" />Исполнители</NavLink></li>
				<li><NavLink to={'#'}><img src="img/menu/applications.svg" alt="applications" />Заявки</NavLink></li>
				<li><NavLink to={'#'}><img src="img/menu/analytics.svg" alt="analytics" />Аналитика бюджета</NavLink></li>
				<li><NavLink to={'#'}><img src="img/menu/add-tenants.svg" alt="add-tenants" />Добавить жильцов</NavLink></li>
				<li><NavLink to={'#'}><img src="img/menu/cctv.svg" alt="cctv" />Видеонаблюдение</NavLink></li>
				<li><NavLink to={'#'}><img src="img/menu/survey.svg" alt="survey" />Опрос</NavLink></li>
				<li><NavLink to={'#'}><img src="img/menu/resident-Ideas.svg" alt="resident-Ideas" />Идеи жильцов</NavLink></li>
				<li><NavLink to={'#'}><img src="img/menu/poll-results.svg" alt="poll-results" />Результаты опросов</NavLink></li>
				<li><NavLink to={'#'}><img src="img/menu/chat.svg" alt="chat" />Чат с жильцами</NavLink></li>
				<li><NavLink to={'#'}><img src="img/menu/payment.svg" alt="payment" />Оплата ком.услуг</NavLink></li>
				<li><NavLink to={'#'}><img src="img/menu/settings.svg" alt="aettings" />Настройки</NavLink></li>
			</ul>
			<h3 className="go-out"><img src="img/menu/go-out.svg" alt="go-out" />Выйти</h3>
		</div>
	)

}

export default Menu;