document.addEventListener('DOMContentLoaded', function() {
    const fetchTweetsButton = document.getElementById('fetch-tweets');
    const tweetsContainer = document.getElementById('tweets-container');

    fetchTweetsButton.addEventListener('click', function() {
        fetch('/api/tweets')
            .then(response => response.json())
            .then(data => {
                tweetsContainer.innerHTML = '';
                data.forEach(tweet => {
                    const tweetDiv = document.createElement('div');
                    tweetDiv.className = 'tweet';
                    tweetDiv.innerHTML = `
                        <strong>${tweet['Username']}</strong><br>
                        <em>${tweet['Created At']}</em><br>
                        <p>${tweet['Tweet']}</p>
                        <p><strong>Category:</strong> ${tweet['Category']}</p>
                        <p><strong>Location:</strong> ${tweet['Location']}</p>
                        <p><strong>Retweets:</strong> ${tweet['Retweet Count']} <strong>Favorites:</strong> ${tweet['Favorite Count']}</p>
                    `;
                    tweetsContainer.appendChild(tweetDiv);
                });
            })
            .catch(error => console.error('Error fetching tweets:', error));
    });

    const fetchNewsButton = document.getElementById('fetch-news');
    const newsContainer = document.getElementById('news-container');

    fetchNewsButton.addEventListener('click', function() {
        fetch('/api/news')
            .then(response => response.json())
            .then(data => {
                newsContainer.innerHTML = '';
                data.forEach(article => {
                    const articleDiv = document.createElement('div');
                    articleDiv.className = 'news-article';
                    articleDiv.innerHTML = `
                        <strong>${article['Source']}</strong><br>
                        <a href="${article['URL']}" target="_blank">${article['Title']}</a><br>
                        <p>${article['Description']}</p>
                        <p><strong>Published At:</strong> ${article['Published At']}</p>
                        <p><strong>Category:</strong> ${article['Category']}</p>
                        <p><strong>Location:</strong> ${article['Location']}</p>
                    `;
                    newsContainer.appendChild(articleDiv);
                });
            })
            .catch(error => console.error('Error fetching news:', error));
    });
});
