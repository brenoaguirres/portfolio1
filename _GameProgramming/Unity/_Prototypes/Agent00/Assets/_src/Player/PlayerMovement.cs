using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.InputSystem;

public class PlayerMovement : MonoBehaviour
{
    [SerializeField]
    private float movementSpeed = 5f;
    private Rigidbody playerRigidbody;
    private Animator playerAnimator;

    private void Start() {
        playerRigidbody = GetComponent<Rigidbody>();
        playerAnimator = GetComponent<Animator>();
    }

    private void FixedUpdate() {
        Vector2 leftStickInput = InputSystem.GetDevice<Gamepad>().leftStick.ReadValue();
        float horizontalInput = leftStickInput.x;
        float verticalInput = leftStickInput.y;

        MovePlayer(horizontalInput, verticalInput);
        UpdateAnimatorParameters(horizontalInput, verticalInput);
    }

    private void MovePlayer(float horizontalInput, float verticalInput) {
        Debug.Log("H: " + horizontalInput.ToString());
        Debug.Log("V: " + verticalInput.ToString());
        Vector3 movementDirection = new Vector3(0, 0, 0);

        if (Mathf.Abs(horizontalInput) > Mathf.Abs(verticalInput)) {
            movementDirection = transform.right * horizontalInput;
        }
        else {
            movementDirection = transform.forward * verticalInput;
        }

        movementDirection = movementDirection.normalized;

        Vector3 movement = movementDirection * movementSpeed * Time.fixedDeltaTime;
        Vector3 newPosition = playerRigidbody.position + movement;
        playerRigidbody.MovePosition(newPosition);
    }

    private void UpdateAnimatorParameters(float horizontalInput, float verticalInput) {
        bool isMoving = Mathf.Abs(horizontalInput) > 0.1f || Mathf.Abs(verticalInput) > 0.1f;
        playerAnimator.SetBool("Move", isMoving);

        playerAnimator.SetFloat("MoveX", horizontalInput);
        playerAnimator.SetFloat("MoveY", verticalInput);
    }
}
