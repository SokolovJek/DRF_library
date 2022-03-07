import logo from './logo.svg';
import './App.css';
import React from 'react';
import AuthorList from './components/Author.js'
import axios from 'axios'

class App extends React.Component {
	constructor(props) {
		super(props)
		this.state = {
			'authors': []
		}
	}

	componentDidMount() {
		axios.get('http://127.0.0.1:8000/api/author/')
			.then(response => {
				const authors = response.data
				console.log('-----------my-----response----------------' + response.data)
				this.setState(
					{ 'authors': authors }
				)

			}).catch(error => console.log('-----------my-----error----------------' + error))
	}

	render() {
		return (
			<div className='container header'>
				<div className='row'>
					<div className='col-12'>
						<h1 className='text-center text-white'>
							Все пользователи с сайта
						</h1>
						<a href='http://127.0.0.1:8000/api/author/' className='btn itd_play text-uppercase'>Перейти</a>
					</div>

				</div>

				<AuthorList authors={this.state.authors} />
				 
			</div>

		)

	}
}


export default App;
