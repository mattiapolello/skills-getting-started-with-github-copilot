"""Tests for POST /activities/{activity_name}/signup endpoint"""


def test_signup_for_activity(client):
    """Test signing up a student for an activity"""
    # Arrange
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity_name}/signup", params={"email": email})

    # Assert
    assert response.status_code == 200
    result = response.json()
    assert "message" in result
    assert email in result["message"]
    assert activity_name in result["message"]

    # Verify participant was added
    activities = client.get("/activities").json()
    assert email in activities[activity_name]["participants"]
