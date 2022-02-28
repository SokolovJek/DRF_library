import React from 'react'


const AuthorItem = ({author}) => {
	return (
		<tr>
			<td>
				{author.first_name}
			</td>
			<td>
				{author.last_name}
			</td>
			<td>
				{author.birthday_year}
			</td>
			<td>
				{author.email}
			</td>
		</tr>
		)
}


const AuthorList = ({authors}) => {
    return(
        <table className='Table'>
            <tbody>
                <tr>
                    <th>
                            Имя
                    </th>
                    <th>
                        Фамилия
                    </th>
                    <th>
                        Год рождения
                    </th>
                    <th>
                        эл. почта
                    </th>
                </tr>

                {authors.map((author) => <AuthorItem author={author}/>)}

            </tbody>
        </table>
	)
}

export default AuthorList;