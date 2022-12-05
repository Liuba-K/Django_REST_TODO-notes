import React from 'react';

const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>
                {project.name_project}
            </td>
            <td>
                {project.users} //точно наследуем от project
            </td>
        </tr>
    )
}

const ProjectList = ({projects}) => {
    return (
        <table>
            <th>
                Project name
            </th>
            <th>
                User
            </th>
            {projects.map((project) => <ProjectItem project={project} />)}
        </table>
    )
}

export default ProjectList;
