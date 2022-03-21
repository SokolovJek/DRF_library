import React from 'react'


const TodoItem = ({todo}) => {
	return (
		<tr>
			<td>
				{todo.project}
			</td>
			<td>
				{todo.users}
			</td>
			<td>
				{todo.todo_descriptions}
			</td>
			<td>
				{todo.is_active}
			</td>
			<td>
				{todo.date_create}
			</td>
			<td>
				{todo.date_update}
			</td>
		</tr>
		)
}


const TodosList = ({todos}) => {
    return(
        <table className='Table'>
            <tbody>
                <tr>
                    <th>
                          проэкт
                    </th>
                    <th>
                        создатель заметки
                    </th>
                    <th>
                        описание
                    </th>
                    <th>
                        статус
                    </th>
                    <th>
                        дата создания
                    </th>
                    <th>
                        дата обновления
                    </th>
                </tr>

                {todos.map((todo) => <TodoItem todo={todo}/>)}

            </tbody>
        </table>
	)
}

export default TodosList;