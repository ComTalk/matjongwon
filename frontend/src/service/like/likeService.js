import axios from "axios";

export default Object.freeze({

    like(params) {
      return true;
        // return axios.get('/v1/like/',{params:params})
        //     .then(response => {
        //         return response.data.documents;
        //     })
        //     .catch(err => {
        //         console.log(err);
        //         alert(err);
        //     });
    },

});