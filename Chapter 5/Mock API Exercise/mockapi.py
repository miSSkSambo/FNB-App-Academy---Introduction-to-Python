import requests

# Replace this with your own MockAPI Album resource URL.
API_ENDPOINT = "https://6adf2e7f8e42963c8d5d8f07.mockapi.io/Album"


def get_songs():
    """GET: Retrieve all songs."""
    try:
        response = requests.get(API_ENDPOINT, timeout=15)
        response.raise_for_status()

        print("\n========== GET SONGS ==========")
        print("Status code:", response.status_code)
        print("Songs:", response.json())

        return response.json()

    except requests.exceptions.RequestException as error:
        print("GET request failed:", error)
        return None


def add_song(song):
    """POST: Create a new song."""
    try:
        response = requests.post(
            API_ENDPOINT,
            json=song,
            timeout=15
        )
        response.raise_for_status()

        print("\n========== POST SONG ==========")
        print("Status code:", response.status_code)
        print("Created song:", response.json())

        return response.json()

    except requests.exceptions.RequestException as error:
        print("POST request failed:", error)
        return None


def update_song(song_id, song):
    """PUT: Replace an existing song."""
    try:
        response = requests.put(
            f"{API_ENDPOINT}/{song_id}",
            json=song,
            timeout=15
        )
        response.raise_for_status()

        print("\n========== PUT SONG ==========")
        print("Status code:", response.status_code)
        print("Updated song:", response.json())

        return response.json()

    except requests.exceptions.RequestException as error:
        print("PUT request failed:", error)
        return None


def delete_song(song_id):
    """DELETE: Remove a song."""
    try:
        response = requests.delete(
            f"{API_ENDPOINT}/{song_id}",
            timeout=15
        )
        response.raise_for_status()

        print("\n========== DELETE SONG ==========")
        print("Status code:", response.status_code)
        print("Deleted song:", response.json())

        return True

    except requests.exceptions.RequestException as error:
        print("DELETE request failed:", error)
        return False


def confirm_deleted(song_id):
    """Check that the deleted song now returns an HTTP error."""
    try:
        response = requests.get(
            f"{API_ENDPOINT}/{song_id}",
            timeout=15
        )
        response.raise_for_status()

        print("The song still exists.")
        print("Status code:", response.status_code)

    except requests.exceptions.HTTPError as error:
        print("\n========== DELETE CONFIRMATION ==========")
        print("Deleted song returned an HTTP error.")
        print("Status code:", error.response.status_code)

    except requests.exceptions.RequestException as error:
        print("Confirmation request failed:", error)


def main():
    # 1. GET: Retrieve the existing songs.
    songs = get_songs()

    if not isinstance(songs, list) or len(songs) < 2:
        print("Add at least two songs before running this exercise.")
        return

    # Use actual IDs returned by MockAPI.
    songs_with_ids = [
        song for song in songs
        if song.get("id")
    ]

    if len(songs_with_ids) < 2:
        print("At least two songs must have valid IDs.")
        print("Create the songs through MockAPI or POST requests.")
        return

    # 2. POST: Add a new song.
    new_song = {
        "name": "Thinking Out Loud",
        "rate": "9"
    }

    add_song(new_song)

    # 3. PUT: Replace the first existing song.
    song_to_update = songs_with_ids[0]["id"]

    updated_song = {
        "name": "Updated Song - Remastered",
        "rate": "10"
    }

    update_song(song_to_update, updated_song)

    # 4. DELETE: Remove the second existing song.
    song_to_delete = songs_with_ids[1]["id"]

    deleted = delete_song(song_to_delete)

    # Immediately check the deleted song's ID.
    if deleted:
        confirm_deleted(song_to_delete)

    # 5. GET: Display the final list.
    print("\n========== FINAL SONG LIST ==========")
    get_songs()


if __name__ == "__main__":
    main()
