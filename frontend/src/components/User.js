import React from 'react';

const UserItem = ({user}) => {
    return (
        <tr>
            <td>
                {user.firstname}
            </td>
            <td>
                {user.lastname}
            </td>
            <td>
                {user.birthday_year}
            </td>
        </tr>
    )
}

const UserList = ({users}) => {
    return (
        <table>
            <th>
                First name
            </th>
            <th>
                Last Name
            </th>

            {users.map((user) => <UserItem user={user} />)}
        </table>
    )
}

export default UserList;
