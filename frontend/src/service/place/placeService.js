import axios from "axios";

export default Object.freeze({

    fetchPlaceList(params) {
        return axios.get('/v1/place/',{params:params})
            .then(response => {
                return response.data.documents;
            })
            .catch(err => {
                console.log(err);
                alert(err);
            });
    },

});