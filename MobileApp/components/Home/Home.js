import {
    View,
    Text,
    ActivityIndicator,
    TouchableOpacity,
    Image,
    ScrollView
} from "react-native";
import mystyles from "../../styles/mystyles";
import Style from "./Style";
import { useEffect, useState } from "react";
import API, { endpoints } from "../../configs/API";

const Home = () => {
    const [courses, setCourses] = useState(null);

    useEffect(() => {
        const loadCourses = async () => {
            try {
                let res = await API.get(endpoints["courses"]);
                setCourses(res.data.results);
            } catch (ex) {
                console.error(ex);
            }
        };
        loadCourses();
    }, []);

    return (
        <View style={mystyles.container}>
            <Text style={Style.subject}>HOME</Text>
            <ScrollView>
                {courses === null ? (
                    <ActivityIndicator />
                ) : (
                    <>
                        {courses.map((c) => (
                            <View
                                key={c.id}
                                style={{ flex: 1, flexDirection: "row" }}
                            >
                                <Image
                                    style={{
                                        width: 60,
                                        height: 60,
                                        margin: 10
                                    }}
                                    source={{ uri: c.image }}
                                />
                                <TouchableOpacity>
                                    <Text style={{ margin: 10 }}>
                                        {c.subject}
                                    </Text>
                                </TouchableOpacity>
                            </View>
                        ))}
                    </>
                )}
            </ScrollView>
        </View>
    );
};

export default Home;
