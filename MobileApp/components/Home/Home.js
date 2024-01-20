import { View, Text, ActivityIndicator } from "react-native"
import mystyles from "../../styles/mystyles"
import Style from "./Style"
import { useEffect, useState } from "react"
import { endpoints } from "../../configs/API"

const Home = () => {
    const [courses, setCourses] = useState(null)

    useEffect(() => {
        const loadCourses = async () => {
            let url = endpoints['courses'];
            try {
                let res = await API.get(url);
                setCourses(res.data.results);
            }
            catch (ex){
                console.error(ex);
            }
        }
    }, [])

    return (
        <View style={mystyles.container}>
            <Text style={Style.subject}>HOME</Text>
            {courses===null?<ActivityIndicator/>:<>
                {courses.map((c) => (
                    <View key = {c.id}>
                        <Text>{c.subject}</Text>
                    </View>
                ))}
            </>}
        </View>
    )
}

export default Home