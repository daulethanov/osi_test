import React, { useState } from "react";
import './submitYourApplication.css';
import axios from "axios";
import AplicationsInput from "../../input/aplications-input/AplicationsInput";

function SubmitYourApplication() {

	// const applicationFormLeftSelect = ['Не важно', 'Второстепенная', 'Важно'];
	// const [applicationFormLeftSelectActive, setApplicationFormLeftSelectActive] = useState(0);
	const [formLeftSelectOpen, setFormLeftSelectOpen] = useState(false);
	const [applicationFormInput, setApplicationFormInput] = useState('')
	const [applicationFormTexterya, setApplicationFormTexterya] = useState('')
	const [applicationFormName, setApplicationFormName] = useState('')
	const [applicationFormSurname, setApplicationFormSurname] = useState()
	const [applicationFormNumber, setApplicationFormNumber] = useState('')
	const [applicationFormAddress, setApplicationFormAddress] = useState('')
	const [applicationFormWhatsapp, setApplicationFormWhatsapp] = useState()
	const [applicationFormTelegram, setApplicationFormTelegram] = useState('')
	const [necessarilyInput, setNecessarilyInput] = useState(false)
	const [aplicationsAccepted, setAplicationsAccepted] = useState(false)

	// const onClickSelectOpen = () => {
	// 	setFormLeftSelectOpen(!formLeftSelectOpen)
	// }

	// const onClickFormLeftSelectActive = (index) => {
	// 	setApplicationFormLeftSelectActive(index)
	// 	setFormLeftSelectOpen(false)
	// }

	const onAddApplication = (e) => {

		if (applicationFormInput.length > 0
			&& applicationFormTexterya.length > 0
			&& applicationFormName.length > 0
			&& applicationFormSurname.length > 0
			&& applicationFormNumber.length > 0
			&& applicationFormAddress.length > 0) {
			axios.post("http://127.0.0.1/api/v1/problem/create", {
				title: applicationFormInput,
				// level_problem: applicationFormLeftSelect[applicationFormLeftSelectActive],
				description: applicationFormTexterya,
				name: applicationFormName,
				surname: applicationFormSurname,
				number: applicationFormNumber,
				address: applicationFormAddress,
				whatsapp: applicationFormWhatsapp,
				telegram_name: applicationFormTelegram
			})
				.then((response) => {
					console.log(response);
				})
				.catch((error) => {
					console.log(error);
				});

			// setApplicationFormLeftSelectActive(0)
			setApplicationFormInput('')
			setApplicationFormTexterya('')
			setApplicationFormName('')
			setApplicationFormSurname('')
			setApplicationFormNumber()
			setApplicationFormAddress('')
			setApplicationFormWhatsapp()
			setApplicationFormTelegram('')
			setNecessarilyInput(false)
			setAplicationsAccepted(true)
		} else {
			setNecessarilyInput(true)
		}
	}

	const onClickAplicationsAccepted = () => {
		setAplicationsAccepted(false)
	}

	return (
		<div className="submit__your__application">
			<h2>Заявка на исправление проблемы</h2>

			{aplicationsAccepted ? (
				<div className="application__form__accepted">
					<img src="img/applications/check.png" alt="check" />
					<h2>Ваша заявка была отправлена на рассмотрение</h2>
					<button onClick={() => onClickAplicationsAccepted()}>ОК</button>
				</div>
			) : (
				<div className="application__form">
				<div className="application__form__content">
					<div className="application__form__left">
						<h3><img src={necessarilyInput ? "img/applications/necessarily-red.png"  : "img/applications/necessarily-default.png" } alt="necessarily-default" />Где обнаружена проблема</h3>
						<AplicationsInput
							type="text"
							value={applicationFormInput}
							onChange={(e) => setApplicationFormInput(e.target.value)}
						></AplicationsInput>
						<h3><img src={necessarilyInput ? "img/applications/necessarily-red.png"  : "img/applications/necessarily-default.png" } alt="necessarily-default" />Описание проблемы</h3>
						<textarea
							value={applicationFormTexterya}
							onChange={(e) => setApplicationFormTexterya(e.target.value)}
						></textarea>
						{/* <div className="application__form__left__select">
							<h3>Оцените важность проблемы: </h3>
							<div className="form__left__select__block"><span onClick={() => onClickSelectOpen()} className={
								applicationFormLeftSelectActive === 0 ? "application__form__left__select__span-green" :
									applicationFormLeftSelectActive === 1 ? "application__form__left__select__span-yellow" :
										applicationFormLeftSelectActive === 2 ? "application__form__left__select__span-red"
											: ''
							}>
								{applicationFormLeftSelect[applicationFormLeftSelectActive]}</span>
								<div id="form__left__select">
									<ul className={formLeftSelectOpen ? "form__left__select__ul active" : "form__left__select__ul"}>
										{applicationFormLeftSelect.map((applicationFormLeftSelect, index) => (
											<li key={index} onClick={() => onClickFormLeftSelectActive(index)}>{applicationFormLeftSelect}</li>
										))}
									</ul>
								</div>
							</div>
						</div> */}
					</div>
					<div className="application__form__right">
						<h3><img src={necessarilyInput ? "img/applications/necessarily-red.png"  : "img/applications/necessarily-default.png" } alt="necessarily-default" />Имя</h3>
						<AplicationsInput
							type="text"
							value={applicationFormName}
							onChange={(e) => setApplicationFormName(e.target.value)}
						></AplicationsInput>
						<h3><img src={necessarilyInput ? "img/applications/necessarily-red.png"  : "img/applications/necessarily-default.png" } alt="necessarily-default" />Фамилия</h3>
						<AplicationsInput
							type="text"
							value={applicationFormSurname}
							onChange={(e) => setApplicationFormSurname(e.target.value)}
						></AplicationsInput>
						<h3><img src={necessarilyInput ? "img/applications/necessarily-red.png"  : "img/applications/necessarily-default.png" } alt="necessarily-default" />Сотовый телефон</h3>
						<AplicationsInput
							type="tel"
							placeholder="+7**********"
							value={applicationFormNumber}
							onChange={(e) => setApplicationFormNumber(e.target.value)}
							maxLength={11}
						></AplicationsInput>
						<h3><img src={necessarilyInput ? "img/applications/necessarily-red.png"  : "img/applications/necessarily-default.png" } alt="necessarily-default" />Адрес</h3>
						<AplicationsInput
							type="text"
							value={applicationFormAddress}
							onChange={(e) => setApplicationFormAddress(e.target.value)}
						></AplicationsInput>
						<h3>Ватсапп</h3>
						<AplicationsInput
							type="text"
							value={applicationFormWhatsapp}
							onChange={(e) => setApplicationFormWhatsapp(e.target.value)}
							placeholder="+7**********"
							maxLength={11}
						></AplicationsInput>
						<h3>Телеграм (номер или почта)</h3>
						<AplicationsInput
							type="text"
							value={applicationFormTelegram}
							onChange={(e) => setApplicationFormTelegram(e.target.value)}
						></AplicationsInput>
					</div>
				</div>
				<button onClick={() => onAddApplication()}>Отправить заявку</button>
			</div>
			)
			}
		</div>
	)

}

export default SubmitYourApplication;