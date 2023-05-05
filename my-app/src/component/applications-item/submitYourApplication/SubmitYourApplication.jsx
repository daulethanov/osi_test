import React, { useState } from "react";
import './submitYourApplication.css';
import axios from "axios";

function SubmitYourApplication() {

	const applicationFormLeftSelect = ['Не важно', 'Второстепенная', 'Важно'];
	const [applicationFormLeftSelectActive, setApplicationFormLeftSelectActive] = useState(0);
	const [formLeftSelectOpen, setFormLeftSelectOpen] = useState(false);
	const [applicationFormInput, setApplicationFormInput] = useState('')
	const [applicationFormTexterya, setApplicationFormTexterya] = useState('')

	const onChangeApplicationFormInput = (e) => {
		setApplicationFormInput(e.target.value)
	}

	const onChangeApplicationFormTexterya = (e) => {
		setApplicationFormTexterya(e.target.value)
	}

	const onClickSelectOpen = () => {
		setFormLeftSelectOpen(!formLeftSelectOpen)
	}

	const onClickFormLeftSelectActive = (index) => {
		setApplicationFormLeftSelectActive(index)
		setFormLeftSelectOpen(false)
	}

	const onAddApplication = () => {
		axios.post("https://642e6fc62b883abc640da793.mockapi.io/data", { title: applicationFormInput,
		important: applicationFormLeftSelect[applicationFormLeftSelectActive]
	})
      .then((response) => {
        console.log(response);
      })
      .catch((error) => {
        console.log(error);
      });

	  setApplicationFormInput('')
	}



	return (
		<div className="submit__your__application">
			<h2>Заявка на исправление проблемы</h2>
			<div className="application__form">
				<div className="application__form__content">
					<div className="application__form__left">
						<h3>Где обнаружена проблема</h3>
						<input type="text" id=""
							value={applicationFormInput}
							onChange={onChangeApplicationFormInput}
						/>
						<h3>Описание проблемы</h3>
						<textarea 
						value={applicationFormTexterya}
						onChange={onChangeApplicationFormTexterya}
						></textarea>
						<div className="application__form__left__select">
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
						</div>
					</div>
					<div className="application__form__right">
						<h3>Внесите вложения</h3>
						<input type="file" />
					</div>
				</div>
				<button onClick={() => onAddApplication()}>Отправить заявку</button>
			</div>
			
		</div>
	)

}

export default SubmitYourApplication;