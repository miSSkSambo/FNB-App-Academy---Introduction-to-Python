
import requests

# Your MockAPI Album resource URL.
API_ENDPOINT = "https://6adf2e7f8e42963c8d5d8f07.mockapi.io/Album"


def get_songs():
    """GET: Retrieve all songs."""
    try:
        response = requests.get(API_ENDPOINT, timeout=15)
        response.raise_for_status()

        songs = response.json()

        print("\n========== GET SONGS ==========")
        print("Status code:", response.status_code)
        print("Songs:", songs)

        return songs

    except (requests.exceptions.RequestException, ValueError) as error:
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

        created_song = response.json()

        print("\n========== POST SONG ==========")
        print("Status code:", response.status_code)
        print("Created song:", created_song)

        return created_song

    except (requests.exceptions.RequestException, ValueError) as error:
        print("POST request failed:", error)
        return None


def update_song(song_id, song):
    """PUT: Update an existing song."""
    try:
        response = requests.put(
            f"{API_ENDPOINT}/{song_id}",
            json=song,
            timeout=15
        )
        response.raise_for_status()

        updated_song = response.json()

        print("\n========== PUT SONG ==========")
        print("Status code:", response.status_code)
        print("Updated song:", updated_song)

        return updated_song

    except (requests.exceptions.RequestException, ValueError) as error:
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
        print("Deleted song ID:", song_id)

        return True

    except requests.exceptions.RequestException as error:
        print("DELETE request failed:", error)
        return False


def confirm_deleted(song_id):
    """Confirm the deleted song returns an HTTP error."""
    try:
        response = requests.get(
            f"{API_ENDPOINT}/{song_id}",
            timeout=15
        )

        if response.status_code == 404:
            print("\n========== DELETE CONFIRMATION ==========")
            print("The deleted song no longer exists.")
            print("Status code:", response.status_code)
        else:
            response.raise_for_status()
            print("The song still exists.")
            print("Status code:", response.status_code)

    except requests.exceptions.RequestException as error:
        print("Confirmation request failed:", error)


def ensure_songs_have_ids():
    """Create ID-bearing records if existing records have no IDs."""
    songs = get_songs()

    if not isinstance(songs, list):
        print("Unable to retrieve songs. Check your API endpoint.")
        return None

    if len(songs) < 2:
        print("Fewer than two songs found. Adding sample songs...")

        sample_songs = [
            {"name": "Shape of You", "rate": "9"},
            {"name": "Perfect", "rate": "10"},
            {"name": "Castle on the Hill", "rate": "8"}
        ]

        for song in sample_songs:
            add_song(song)

        songs = get_songs()

    # Resource Data records may lack IDs, so copy them through POST.
    songs_without_ids = [
        song for song in songs
        if not song.get("id")
    ]

    if songs_without_ids:
        print("\nCreating API records with generated IDs...")

        for song in songs_without_ids:
            created_song = add_song({
                "name": song.get("name", "Unknown Song"),
                "rate": str(song.get("rate", "0"))
            })

            if created_song is None:
                print("Could not create a record. Stopping.")
                return None

    # Retrieve the records created through POST.
    songs = get_songs()

    if not isinstance(songs, list):
        return None

    songs_with_ids = [
        song for song in songs
        if song.get("id") is not None
        and str(song.get("id")).strip() != ""
    ]

    if len(songs_with_ids) < 2:
        print("At least two songs with IDs are required.")
        return None

    return songs_with_ids


def main():
    # 1. GET: Retrieve songs and ensure they have IDs.
    songs = ensure_songs_have_ids()

    if not songs:
        print("Unable to continue the exercise.")
        return

    # 2. POST: Add a new song.
    add_song({
        "name": "Thinking Out Loud",
        "rate": "9"
    })

    # 3. PUT: Update the first song.
    song_to_update = songs[0]["id"]

    update_song(song_to_update, {
        "name": "Updated Song - Remastered",
        "rate": "10"
    })

    # 4. DELETE: Delete the second song.
    song_to_delete = songs[1]["id"]

    deleted = delete_song(song_to_delete)

    # Confirm deletion by checking for HTTP 404.
    if deleted:
        confirm_deleted(song_to_delete)

    # 5. GET: Display the final list.
    print("\n========== FINAL SONG LIST ==========")
    get_songs()


if __name__ == "__main__":
    main()
