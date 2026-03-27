"""Tests for GET /activities endpoint"""


def test_get_all_activities(client):
    """Test retrieving all activities returns expected structure"""
    # Arrange
    expected_activities = [
        "Chess Club",
        "Programming Class",
        "Gym Class",
        "Basketball",
        "Tennis Club",
        "Art Workshop",
        "Music Ensemble",
        "Debate Club",
        "Science Fair Team",
    ]

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    activities = response.json()
    assert isinstance(activities, dict)
    assert len(activities) == 9
    for activity_name in expected_activities:
        assert activity_name in activities
        activity = activities[activity_name]
        assert "description" in activity
        assert "schedule" in activity
        assert "max_participants" in activity
        assert "participants" in activity
        assert isinstance(activity["participants"], list)
