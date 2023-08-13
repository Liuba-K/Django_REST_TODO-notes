import React from 'react';
import {useParams} from 'react-router-dom';

const ProjectItem = ({project}) => {
     return (
        <tr>
            <td>
                {project.name_project}
            </td>
            <td>
                {project.users}
            </td>
        </tr>
    )
}

const ProjectList = ({projects}) => {
    let {name_project} = useParams();
    console.log(name_project)
    let filter_project = projects.filter((project)=> project.name_project === name_project);
    //let filter_project = projects.filter((project)=> project.name_project === name_project);
    return (
        <table>
            <th>
                Project name
            </th>
            <th>
                User
            </th>
            {filter_project.map((project) => <ProjectItem project={project} />)}
        </table>
    )
}

export default ProjectList;
