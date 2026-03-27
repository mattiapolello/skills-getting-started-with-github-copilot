"""Tests for DELETE /activities/{activity_name}/cancel endpoint"""


def test_cancel_activity_signup(client):
    """Test unregistering a student from an activity"""
    # Arrange
    activity_name = "Tennis Club"
    email = "sarah@mergington.edu"  # Known participant

    # Verify participant exists before deletion
    activities = client.get("/activities").json()
    assert email in activities[activity_name]["participants"]

    # Act
    response = client.delete(f"/activities/{activity_name}/cancel", params={"email": email})

    # Assert
    assert response.status_code == 200
    result = response.json()
    assert "message" in result
    assert email in result["message"]
    assert activity_name in result["message"]

    # Verify participant was removed
    activities = client.get("/activities").json()
    assert email not in activities[activity_name]["participants"]
