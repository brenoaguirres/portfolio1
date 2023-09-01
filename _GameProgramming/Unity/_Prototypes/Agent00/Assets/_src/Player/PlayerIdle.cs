using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.InputSystem;

public class PlayerIdle : MonoBehaviour
{
    private Animator playerAnimator;
    private bool isNotIdle;

    private float idleTimer = 0f;

    private bool hasTriggeredStomp = false;
    private bool hasTriggeredSmoke = false;

    private void Start() {
        playerAnimator = GetComponent<Animator>();
    }

    private void Update() {
        isNotIdle = playerAnimator.GetBool("Move");

        if (isNotIdle) {
            ResetTimer();
        }
        else if (idleTimer >= 12f) {
            ResetTimer();
        }
        else if (idleTimer >= 10f && !hasTriggeredSmoke) {
            playerAnimator.SetTrigger("Smoke");
            hasTriggeredSmoke = true;
        }
        else if (idleTimer >= 5f  && !hasTriggeredStomp) {
            playerAnimator.SetTrigger("Stomp");
            hasTriggeredStomp = true;
        }

        idleTimer += Time.deltaTime;
    }



    private void ResetTimer() {
        idleTimer = 0f;
        hasTriggeredSmoke = false;
        hasTriggeredStomp = false;
    }
}
