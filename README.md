# Music Recommender

![image](https://github.com/NicolasTfile/Music_Recommender/assets/112314081/b9e8bf5d-ff9d-43b6-8a86-ad62c144a6e0)


Music Recommender is a web application that uses the Spotify API to recommend music based on a user's top tracks. It allows users to log in with their Spotify account and discover new music tailored to their preferences.

## Getting Started

Follow these steps to set up and run the Music Recommender web app on your local machine.

### Prerequisites

You need to have the following installed on your system:

- Python 3.x
- pip (Python package manager)

### Installation

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/NicolasTfile/Music_Recommender.git
   cd Music_Recommender
   ```

2. Create a virtual environment (optional but recommended):

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

### Setting Up Spotify API Credentials

To use the Spotify API, you need to obtain your client ID and client secret from the Spotify Developer Dashboard. Follow these steps:

1. Visit the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).

2. Log in with your Spotify account or create one if you don't have an account.

3. Create a new Spotify App in the Dashboard.

4. Once your app is created, note down the **Client ID** and **Client Secret**.

5. Set up environment variables for your credentials:

   #### Using a .env File

   Create a `.env` file in the project root and add your credentials:

   ```
   SPOTIPY_CLIENT_ID=your-client-id
   SPOTIPY_CLIENT_SECRET=your-client-secret
   SPOTIPY_REDIRECT_URI=http://localhost:5000/callback
   ```

   #### Exporting Variables

   Alternatively, you can export the variables directly:

   ```
   export SPOTIPY_CLIENT_ID=your-client-id
   export SPOTIPY_CLIENT_SECRET=your-client-secret
   export SPOTIPY_REDIRECT_URI=http://localhost:5000/callback
   ```

### Running the Application

Now that you've set up everything, you can run the Music Recommender web app:

```
python app.py
```

Open your web browser and navigate to [http://localhost:5000](http://localhost:5000) to access the Music Recommender website.

## How to Use

1. Home Page: The landing page welcomes users to the Music Recommender app and provides an option to log in with Spotify.

2. Login Page: Click "Login with Spotify" to log in using your Spotify account. You'll be redirected to Spotify's authentication page, where you can grant access to your account.

3. Recommendations Page: After logging in, you'll see a list of your top tracks, followed by recommended tracks based on your listening history. You can explore new music recommendations here.

## Environment Variables

- `SPOTIPY_CLIENT_ID`: Your Spotify API client ID.
- `SPOTIPY_CLIENT_SECRET`: Your Spotify API client secret.
- `SPOTIPY_REDIRECT_URI`: The redirect URI for Spotify authentication (set to `http://localhost:5000/callback` by default).

## Contributing

If you'd like to contribute to this project, please fork the repository and create a pull request. You can also report issues or suggest new features by opening an issue.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
