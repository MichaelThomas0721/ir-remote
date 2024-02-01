export default async function SendDataToFlask(data: any, endPoint: string) {
    console.log(data, endPoint);
    // Make a POST request to the Flask API
    await fetch(endPoint, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
        .then(async response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            const res = await response.json()
            return res;
        })
        .then(responseData => {
            // Handle the response from the Flask API
            console.log('API Response:', responseData);
        })
        .catch(error => {
            // Handle any errors that occurred during the fetch
            console.error('Error:', error);
        });
}