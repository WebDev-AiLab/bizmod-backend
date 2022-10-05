export default function template(input_string, data) {
    let templatorRegExp = /\{\{(.*)\}\}/g

    let newInputString = input_string

    let SubDescriptionsVars = input_string?.split(' ')?.map(word => (word?.match(templatorRegExp)?.[0]))

    SubDescriptionsVars.forEach(variable => {

        let varName = ''


        if (variable) {
            varName = variable.slice(2, -2)
            console.log(variable, data?.[varName])
            newInputString = newInputString?.replace(variable, data?.[varName])
        }

    })


    return newInputString

}